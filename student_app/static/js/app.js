/* ==========================================================================
   Data Mining TP Evaluation Platform — SPA JavaScript Controller
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
    // App State
    let selectedTPId = null;
    let studentCode = '';
    let attemptId = null;
    let currentQuestionId = null;
    let secondsRemaining = 20;
    let timerInterval = null;
    let isSubmitting = false;

    const TIMER_FULL_DASH_ARRAY = 264; // SVG circumference 2 * pi * 42

    // DOM Elements
    const screenLogin = document.getElementById('screen-login');
    const screenQuiz = document.getElementById('screen-quiz');
    const screenResults = document.getElementById('screen-results');

    const tpGrid = document.getElementById('tp-grid');
    const startForm = document.getElementById('start-form');
    const codeInput = document.getElementById('student-code-input');
    const btnStartTest = document.getElementById('btn-start-test');

    const alertBanner = document.getElementById('alert-banner');
    const alertMessage = document.getElementById('alert-message');
    const alertClose = document.getElementById('alert-close');

    const userBadge = document.getElementById('user-badge');
    const activeUserCode = document.getElementById('active-user-code');

    const currentPosEl = document.getElementById('current-pos');
    const totalPosEl = document.getElementById('total-pos');
    const progressBarFill = document.getElementById('progress-bar-fill');

    const timerWidget = document.getElementById('timer-widget');
    const timerProgressCircle = document.getElementById('timer-progress-circle');
    const timerDisplayNum = document.getElementById('timer-display-num');

    const questionTextEl = document.getElementById('question-text');
    const btnAnswerTrue = document.getElementById('btn-answer-true');
    const btnAnswerFalse = document.getElementById('btn-answer-false');
    const btnAnswerSkip = document.getElementById('btn-answer-skip');

    const finalScoreVal = document.getElementById('final-score-val');
    const performancePill = document.getElementById('performance-pill');
    const btnReturnHome = document.getElementById('btn-return-home');

    // Cookie Helper Functions for Autofill
    function setCookie(name, value, days = 30) {
        const d = new Date();
        d.setTime(d.getTime() + (days * 24 * 60 * 60 * 1000));
        document.cookie = `${name}=${encodeURIComponent(value)};expires=${d.toUTCString()};path=/`;
        try { localStorage.setItem(name, value); } catch (e) {}
    }

    function getCookie(name) {
        try {
            const localVal = localStorage.getItem(name);
            if (localVal) return localVal;
        } catch (e) {}

        const match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
        return match ? decodeURIComponent(match[2]) : '';
    }

    // Load Saved Student Code from Cookie/localStorage
    function loadSavedStudentCode() {
        const savedCode = getCookie('student_code');
        if (savedCode) {
            codeInput.value = savedCode;
            validateForm();
        }
    }

    // 1. Device Fingerprinting Generator
    function getDeviceFingerprint() {
        const raw = [
            navigator.userAgent,
            navigator.language,
            screen.width + 'x' + screen.height,
            screen.colorDepth,
            new Date().getTimezoneOffset()
        ].join('|');
        
        let hash = 0;
        for (let i = 0; i < raw.length; i++) {
            const char = raw.charCodeAt(i);
            hash = ((hash << 5) - hash) + char;
            hash |= 0;
        }
        return 'fp_' + Math.abs(hash).toString(16);
    }

    const btnResetCooldown = document.getElementById('btn-reset-cooldown');

    // Alert Banner Utility
    function showAlert(msg, isCooldown = false) {
        alertMessage.textContent = msg;
        alertBanner.classList.remove('hidden');
        if (isCooldown) {
            btnResetCooldown.classList.remove('hidden');
        } else {
            btnResetCooldown.classList.add('hidden');
        }
        alertBanner.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    function hideAlert() {
        alertBanner.classList.add('hidden');
        btnResetCooldown.classList.add('hidden');
    }

    if (alertClose) alertClose.addEventListener('click', hideAlert);

    const btnTopResetCooldown = document.getElementById('btn-top-reset-cooldown');

    async function executeResetCooldown() {
        try {
            const code = codeInput ? codeInput.value.trim().toUpperCase() : '';
            const res = await fetch(`/api/dev/reset_cooldown?code=${encodeURIComponent(code)}`, { method: 'POST' });
            if (res.ok) {
                if (typeof cooldownInterval !== 'undefined') clearInterval(cooldownInterval);
                if (topCooldownBar) topCooldownBar.classList.add('hidden');
                hideAlert();
                showAlert('✅ Cooldown reset! You can now start a new evaluation attempt.');
                if (btnStartTest) {
                    btnStartTest.disabled = false;
                    const sp = btnStartTest.querySelector('span');
                    if (sp) sp.textContent = 'Start Timed Test';
                }
            }
        } catch (e) {
            showAlert('Failed to reset cooldown.');
        }
    }

    if (btnResetCooldown) btnResetCooldown.addEventListener('click', executeResetCooldown);
    if (btnTopResetCooldown) btnTopResetCooldown.addEventListener('click', executeResetCooldown);

    let isQuizActive = false;

    // 3. Screen Switching Helper
    function showScreen(screenName) {
        hideAlert();
        
        // Hide all screens
        screenLogin.classList.add('hidden');
        screenLogin.classList.remove('active');
        screenQuiz.classList.add('hidden');
        screenQuiz.classList.remove('active');
        screenResults.classList.add('hidden');
        screenResults.classList.remove('active');

        if (screenName === 'login') {
            isQuizActive = false;
            if (fullscreenOverlay) fullscreenOverlay.classList.add('hidden');
            screenLogin.classList.remove('hidden');
            screenLogin.classList.add('active');
            userBadge.classList.add('hidden');
        } else if (screenName === 'quiz') {
            isQuizActive = true;
            screenQuiz.classList.remove('hidden');
            screenQuiz.classList.add('active');
            userBadge.classList.remove('hidden');
        } else if (screenName === 'results') {
            isQuizActive = false;
            if (fullscreenOverlay) fullscreenOverlay.classList.add('hidden');
            if (document.fullscreenElement) {
                document.exitFullscreen().catch(() => {});
            }
            screenResults.classList.remove('hidden');
            screenResults.classList.add('active');
            userBadge.classList.remove('hidden');
        }
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // 4. Fetch Available TPs
    async function loadTPs() {
        try {
            const res = await fetch('/api/tps');
            if (!res.ok) throw new Error('Failed to load TPs');
            const tps = await res.json();

            tpGrid.innerHTML = '';
            tps.forEach(tp => {
                const card = document.createElement('div');
                card.className = 'tp-card';
                card.dataset.tpId = tp.id;
                card.innerHTML = `
                    <div class="tp-icon-box"><i class="fa-solid fa-folder-open"></i></div>
                    <div class="tp-details">
                        <span>TP ${tp.id} Evaluation</span>
                        <small>${tp.name.split(':')[1] || tp.name}</small>
                    </div>
                `;

                card.addEventListener('click', () => {
                    document.querySelectorAll('.tp-card').forEach(c => c.classList.remove('selected'));
                    card.classList.add('selected');
                    selectedTPId = tp.id;
                    hideAlert();
                    validateForm();
                });

                tpGrid.appendChild(card);
            });
        } catch (err) {
            tpGrid.innerHTML = `<div class="text-danger">Error loading TPs. Please refresh page.</div>`;
        }
    }

    function validateForm() {
        const code = codeInput.value.trim();
        // Enable button whenever user types at least 2 characters
        btnStartTest.disabled = (code.length < 2);
    }

    if (codeInput) {
        codeInput.addEventListener('input', () => {
            hideAlert();
            validateForm();
        });
    }

    const topCooldownBar = document.getElementById('top-cooldown-bar');
    const topCooldownTimer = document.getElementById('top-cooldown-timer');

    // Disable text copying, context menu, and dragging on quiz screen
    if (screenQuiz) {
        ['copy', 'cut', 'contextmenu', 'dragstart', 'selectstart'].forEach(eventType => {
            screenQuiz.addEventListener(eventType, (e) => {
                e.preventDefault();
                return false;
            });
        });
    }

    let cooldownInterval = null;

    function startCooldownTimer(remainingSec) {
        clearInterval(cooldownInterval);
        btnStartTest.disabled = true;
        if (topCooldownBar) topCooldownBar.classList.remove('hidden');

        function updateDisplay() {
            if (remainingSec <= 0) {
                clearInterval(cooldownInterval);
                if (topCooldownBar) topCooldownBar.classList.add('hidden');
                showAlert('✅ Cooldown finished! You can now start your evaluation test.');
                btnStartTest.disabled = false;
                btnStartTest.querySelector('span').textContent = 'Start Timed Test';
                return;
            }

            const mins = Math.floor(remainingSec / 60);
            const secs = remainingSec % 60;
            const timeStr = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
            
            if (topCooldownTimer) topCooldownTimer.textContent = timeStr;
            btnStartTest.querySelector('span').textContent = 'Start Timed Test';
            remainingSec--;
        }

        updateDisplay();
        cooldownInterval = setInterval(updateDisplay, 1000);
    }

    // 5. Start Quiz Attempt
    if (startForm) {
        startForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            hideAlert();

        studentCode = codeInput.value.trim().toUpperCase();

        if (!studentCode) {
            showAlert('Please enter your student identifier code.');
            codeInput.focus();
            return;
        }

        if (selectedTPId === null) {
            showAlert('⚠️ Please select a TP evaluation card from the options above to begin.');
            tpGrid.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
            return;
        }

        btnStartTest.disabled = true;
        btnStartTest.querySelector('span').textContent = 'Validating Code...';

        try {
            const res = await fetch('/api/attempt/start', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    code: studentCode,
                    tp_id: selectedTPId,
                    device_fingerprint: getDeviceFingerprint(),
                    user_agent: navigator.userAgent
                })
            });

            const data = await res.json();

            if (!res.ok) {
                if (res.status === 429) {
                    let sec = 600;
                    const match = data.detail ? data.detail.match(/\((\d+)s remaining\)/) : null;
                    if (match) {
                        sec = parseInt(match[1]);
                    } else if (res.headers.get('X-Cooldown-Remaining-Sec')) {
                        sec = parseInt(res.headers.get('X-Cooldown-Remaining-Sec'));
                    }
                    showAlert(data.detail || `⏳ Cooldown active. Please wait ${sec}s before starting another attempt.`, true);
                    startCooldownTimer(sec);
                } else {
                    showAlert(data.detail || `Wrong student code typed: '${studentCode}'. Please check your code.`);
                    btnStartTest.disabled = false;
                    btnStartTest.querySelector('span').textContent = 'Start Timed Test';
                }
                return;
            }

            // Save valid student code in Cookie & localStorage for autofill
            setCookie('student_code', studentCode, 30);

            attemptId = data.attempt_id;
            currentViolationCount = 0;
            activeUserCode.textContent = studentCode + ' (TP ' + selectedTPId + ')';
            
            showScreen('quiz');
            requestFullscreenMode();
            fetchNextQuestion();

        } catch (err) {
            showAlert('Server connection error. Please verify server is running.');
            btnStartTest.disabled = false;
            btnStartTest.querySelector('span').textContent = 'Start Timed Test';
        }
    });
}

    // Auto-finish attempt if student refreshes or exits page during active quiz
    window.addEventListener('beforeunload', () => {
        if (attemptId && screenQuiz.classList.contains('active')) {
            navigator.sendBeacon(`/api/attempt/${attemptId}/finish`);
        }
    });

    // Anti-Cheat Violation Manager & Toast System
    const fullscreenOverlay = document.getElementById('fullscreen-overlay');
    const btnReenterFullscreen = document.getElementById('btn-reenter-fullscreen');
    const violationToast = document.getElementById('violation-toast');
    const violationBadge = document.getElementById('violation-badge');
    const violationDesc = document.getElementById('violation-desc');

    let currentViolationCount = 0;
    let violationToastTimeout = null;

    function requestFullscreenMode() {
        try {
            const docEl = document.documentElement;
            if (docEl.requestFullscreen) {
                docEl.requestFullscreen().catch(err => {
                    console.warn("Fullscreen request rejected/unsupported:", err);
                });
            }
        } catch (e) {}
    }

    if (btnReenterFullscreen) {
        btnReenterFullscreen.addEventListener('click', () => {
            requestFullscreenMode();
        });
    }

    document.addEventListener('fullscreenchange', () => {
        if (screenQuiz.classList.contains('active') && isQuizActive) {
            if (!document.fullscreenElement) {
                if (fullscreenOverlay) fullscreenOverlay.classList.remove('hidden');
                reportViolationEvent("fullscreen_exit", "Exited fullscreen mode");
            } else {
                if (fullscreenOverlay) fullscreenOverlay.classList.add('hidden');
            }
        } else {
            if (fullscreenOverlay) fullscreenOverlay.classList.add('hidden');
        }
    });

    let isEndTestModalOpen = false;

    function reportViolationEvent(eventType, details) {
        if (!attemptId || !screenQuiz.classList.contains('active') || isEndTestModalOpen || !isQuizActive) return;

        const payload = JSON.stringify({ event_type: eventType, details: details });
        if (navigator.sendBeacon) {
            navigator.sendBeacon(`/api/attempt/${attemptId}/event`, new Blob([payload], { type: 'application/json' }));
        } else {
            fetch(`/api/attempt/${attemptId}/event`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: payload
            }).catch(() => {});
        }

        currentViolationCount++;
        showViolationToast(eventType, details, currentViolationCount);

        if (currentViolationCount >= 4) {
            clearInterval(timerInterval);
            setTimeout(() => {
                finishQuizEarlyDueToViolations();
            }, 600);
        }
    }

    function showViolationToast(eventType, details, count) {
        if (!violationToast) return;
        clearTimeout(violationToastTimeout);
        if (violationBadge) violationBadge.textContent = `Warning ${count}/4`;
        if (violationDesc) violationDesc.textContent = `${details || eventType}!`;
        violationToast.classList.remove('hidden');

        violationToastTimeout = setTimeout(() => {
            violationToast.classList.add('hidden');
        }, 4000);
    }

    async function finishQuizEarlyDueToViolations() {
        clearInterval(timerInterval);
        try {
            await fetch(`/api/attempt/${attemptId}/finish`, { method: 'POST' });
        } catch (e) {}
        finishAttempt();
    }

    // Monitor Page Visibility & Window Focus
    document.addEventListener('visibilitychange', () => {
        if (document.hidden && screenQuiz.classList.contains('active')) {
            reportViolationEvent("tab_hidden", "Switched tab or minimized browser window");
        }
    });

    window.addEventListener('blur', () => {
        if (screenQuiz.classList.contains('active')) {
            reportViolationEvent("window_blur", "Window focus lost");
        }
    });

    // Monitor Mouse Leaving Viewport
    document.addEventListener('mouseleave', (e) => {
        if (screenQuiz.classList.contains('active') && e.clientY <= 0) {
            reportViolationEvent("mouse_left_viewport", "Mouse exited top of window");
        }
    });

    // Prevent Context Menu & Shortcut Keys
    document.addEventListener('contextmenu', (e) => {
        if (screenQuiz.classList.contains('active')) {
            e.preventDefault();
            reportViolationEvent("copy_or_context_menu_attempt", "Right-click context menu attempt");
            return false;
        }
    });

    document.addEventListener('keydown', (e) => {
        if (!screenQuiz.classList.contains('active')) return;

        const key = e.key.toLowerCase();
        const isCmdCtrl = e.ctrlKey || e.metaKey;

        if (isCmdCtrl && (key === 'c' || key === 'v' || key === 'u' || key === 'a' || key === 's' || key === 'p')) {
            e.preventDefault();
            reportViolationEvent("shortcut_attempt", `Keyboard shortcut Ctrl+${key.toUpperCase()} attempt`);
            return false;
        }

        if (e.key === 'F12' || (isCmdCtrl && e.shiftKey && (key === 'i' || key === 'j' || key === 'c'))) {
            e.preventDefault();
            reportViolationEvent("shortcut_attempt", "Developer tools shortcut attempt");
            return false;
        }
    });

    // 6. Fetch Next Question
    function renderQuestionPayload(data) {
        if (!data) return;

        if (data.finished) {
            finishAttempt();
            return;
        }

        // Render Question & Dynamic Options Order
        currentQuestionId = data.question_id;
        questionTextEl.textContent = data.text;
        
        currentPosEl.textContent = data.position;
        totalPosEl.textContent = data.total;

        const progressPct = (data.position / data.total) * 100;
        progressBarFill.style.width = `${progressPct}%`;

        // Render Randomized True/False Button Order
        const optionsContainer = document.querySelector('.answers-grid');
        if (optionsContainer && data.options && Array.isArray(data.options)) {
            optionsContainer.innerHTML = '';
            data.options.forEach(optVal => {
                const btn = document.createElement('button');
                btn.type = 'button';
                btn.className = `btn btn-choice ${optVal ? 'btn-true' : 'btn-false'}`;
                btn.id = optVal ? 'btn-answer-true' : 'btn-answer-false';
                btn.innerHTML = optVal 
                    ? '<i class="fa-solid fa-check"></i><span>TRUE</span>' 
                    : '<i class="fa-solid fa-xmark"></i><span>FALSE</span>';
                btn.onclick = () => submitAnswer(optVal);
                optionsContainer.appendChild(btn);
            });
        }

        const btnSkip = document.getElementById('btn-answer-skip');
        if (btnSkip) btnSkip.disabled = false;
        isSubmitting = false;

        // Start 20s Timer
        startQuestionTimer();
    }

    async function fetchNextQuestion() {
        clearInterval(timerInterval);
        isSubmitting = false;

        try {
            const res = await fetch(`/api/attempt/${attemptId}/next-question`);
            const data = await res.json();

            if (!res.ok) {
                showAlert(data.detail || 'Error loading question.');
                return;
            }

            renderQuestionPayload(data);

        } catch (err) {
            showAlert('Network error fetching next question.');
        }
    }

    // 7. 20s Visual Countdown Timer
    function startQuestionTimer() {
        secondsRemaining = 20;
        updateTimerUI();

        timerInterval = setInterval(() => {
            secondsRemaining--;
            updateTimerUI();

            if (secondsRemaining <= 0) {
                clearInterval(timerInterval);
                // Expiry auto-submit null
                submitAnswer(null);
            }
        }, 1000);
    }

    function updateTimerUI() {
        timerDisplayNum.textContent = secondsRemaining;

        // Calculate SVG offset
        const fraction = secondsRemaining / 20;
        const dashoffset = TIMER_FULL_DASH_ARRAY * (1 - fraction);
        timerProgressCircle.style.strokeDashoffset = dashoffset;

        // Color states
        timerWidget.classList.remove('warning', 'danger');
        if (secondsRemaining <= 5) {
            timerWidget.classList.add('danger');
        } else if (secondsRemaining <= 10) {
            timerWidget.classList.add('warning');
        }
    }

    // 8. Submit Answer (Fast Unified Transaction)
    async function submitAnswer(chosenValue) {
        if (isSubmitting) return;
        isSubmitting = true;
        clearInterval(timerInterval);

        const allBtns = document.querySelectorAll('.answers-grid button, #btn-answer-skip');
        allBtns.forEach(b => b.disabled = true);

        try {
            const res = await fetch(`/api/attempt/${attemptId}/answer-and-next`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    question_id: currentQuestionId,
                    chosen: chosenValue
                })
            });

            if (!res.ok) {
                fetchNextQuestion();
                return;
            }

            const data = await res.json();
            renderQuestionPayload(data.next_question);

        } catch (err) {
            showAlert('Failed to transmit answer. Retrying...');
            fetchNextQuestion();
        }
    }

    if (btnAnswerTrue) btnAnswerTrue.addEventListener('click', () => submitAnswer(true));
    if (btnAnswerFalse) btnAnswerFalse.addEventListener('click', () => submitAnswer(false));
    if (btnAnswerSkip) {
        btnAnswerSkip.addEventListener('click', () => submitAnswer(null));
    }

    const endTestModal = document.getElementById('end-test-modal');
    const btnCancelEndTest = document.getElementById('btn-cancel-end-test');
    const btnConfirmEndTest = document.getElementById('btn-confirm-end-test');
    const btnExitTest = document.getElementById('btn-exit-test');

    if (btnExitTest) {
        btnExitTest.addEventListener('click', () => {
            isEndTestModalOpen = true;
            if (endTestModal) endTestModal.classList.remove('hidden');
        });
    }

    if (btnCancelEndTest) {
        btnCancelEndTest.addEventListener('click', () => {
            isEndTestModalOpen = false;
            if (endTestModal) endTestModal.classList.add('hidden');
        });
    }

    if (btnConfirmEndTest) {
        btnConfirmEndTest.addEventListener('click', () => {
            isEndTestModalOpen = false;
            if (endTestModal) endTestModal.classList.add('hidden');
            isQuizActive = false;
            if (fullscreenOverlay) fullscreenOverlay.classList.add('hidden');
            finishAttempt();
        });
    }

    // 9. Finish Quiz Attempt
    async function finishAttempt() {
        isQuizActive = false;
        if (fullscreenOverlay) fullscreenOverlay.classList.add('hidden');
        if (document.fullscreenElement) {
            document.exitFullscreen().catch(() => {});
        }
        clearInterval(timerInterval);
        try {
            const res = await fetch(`/api/attempt/${attemptId}/finish`, {
                method: 'POST'
            });
            const data = await res.json();

            if (!res.ok) {
                showAlert(data.detail || 'Error finalizing evaluation.');
                return;
            }

            // Display Results
            const mark = data.final_mark.toFixed(1);
            finalScoreVal.textContent = mark;

            document.getElementById('res-correct-count').textContent = data.correct_count || 0;
            document.getElementById('res-wrong-count').textContent = data.wrong_count || 0;
            document.getElementById('res-skipped-count').textContent = data.skipped_count || 0;

            if (data.final_mark >= 10.0) {
                performancePill.className = 'performance-pill pill-pass';
                performancePill.textContent = mark >= 16 ? 'Excellent Pass' : (mark >= 14 ? 'Very Good' : 'Pass');
            } else {
                performancePill.className = 'performance-pill pill-fail';
                performancePill.textContent = 'Needs Improvement';
            }

            showScreen('results');

        } catch (err) {
            showAlert('Error submitting test results.');
        }
    }

    // 10. Return Home Button
    if (btnReturnHome) {
        btnReturnHome.addEventListener('click', () => {
            selectedTPId = null;
            attemptId = null;
            currentQuestionId = null;
            if (btnStartTest) {
                btnStartTest.disabled = false;
                const sp = btnStartTest.querySelector('span');
                if (sp) sp.textContent = 'Start Timed Test';
            }
            document.querySelectorAll('.tp-card').forEach(c => c.classList.remove('selected'));
            showScreen('login');
            loadSavedStudentCode();
        });
    }

    // Init App
    loadTPs();
    loadSavedStudentCode();
    showScreen('login');
});
