// ===============================================
// HUMAN DESIGN EMOTIONAL MANIFESTO
// Interactive JavaScript for 5/1 Manifesting Generator
// ===============================================

// Daily Affirmations Pool
const affirmations = [
    "I honor my emotional wave and trust that clarity comes in divine timing.",
    "My sacral gut knows what is correct for me. I wait to respond with confidence.",
    "I am powerful in the present moment. My instincts under pressure are my superpower.",
    "I investigate deeply before sharing. My expertise comes from solid foundations.",
    "My solutions work best when others recognize my value and invite my input.",
    "I give myself permission to ride my emotional wave from high to low before deciding.",
    "There is no truth in the now for me. Days or weeks of feeling reveal my path.",
    "I trust my immediate gut responses and stay fully present rather than overthinking.",
    "I transmit truth and value when the timing is right. My influence ripples outward.",
    "I am a Master Synthesizer, transforming life's complexity into clear wisdom.",
    "My emotional clarity deepens my decision-making. I embrace my feeling waves.",
    "I move with speed once clarity arrives. My Manifesting Generator energy is powerful.",
    "I inform others before acting, creating smooth manifestation and preventing resistance.",
    "My Channel 34-57 makes me remarkably powerful under pressure. I trust my instincts.",
    "My Channel 26-44 gives me natural entrepreneurial wisdom. I share what benefits others.",
    "I question assumptions with Gate 63's healthy skepticism. Logic guides my path.",
    "I focus intensely with Gate 9's concentrated power. Mastery comes through repetition.",
    "I express my expertise with Gate 16's enthusiastic passion. My skills inspire others.",
    "Gate 64 transforms my mental confusion into breakthrough insights. Chaos becomes clarity.",
    "I am the Heretic who challenges conventional wisdom with universal solutions.",
    "I am the Investigator who builds confidence through thorough understanding.",
    "My Line 5 nature means others project leadership onto me. I embrace this responsibility wisely.",
    "My Line 1 foundation requires deep research. I honor my need for solid knowledge.",
    "I experience satisfaction when I follow my responses correctly. This is my alignment.",
    "I experience peace when I move efficiently toward my goals. This is my flow.",
    "Frustration is my signal that I'm initiating instead of responding. I course-correct with grace.",
    "I work in natural cycles of intense focus followed by rest. This rhythm sustains me.",
    "My mental activity comes in waves. I don't force constant output.",
    "Physical exercise helps me process mental energy. Movement integrates my wisdom.",
    "Time in nature resets my sensitive system. I prioritize connection with the earth.",
    "I communicate my need for processing time. Others understand when I explain my design.",
    "My strong instincts may seem abrupt to others. I help them understand my internal experience.",
    "I seek environments that value quality over quantity and recognize my expertise.",
    "My natural paths include research, crisis management, teaching, and pattern recognition.",
    "I am designed to respond powerfully to opportunities life presents.",
    "I can move quickly and skip steps that pure Generators must take.",
    "My undefined Head center makes me wise about which questions are truly worth pursuing.",
    "My undefined Ajna provides mental flexibility to see multiple perspectives.",
    "My undefined G-Center helps me understand diverse ways of expressing love and purpose.",
    "My undefined Heart center creates wisdom about what's truly worth proving.",
    "My undefined Spleen makes me ultimately wise about health, fear, and survival instincts.",
    "My defined Sacral provides sustainable work energy and creative life force.",
    "My defined Throat offers dependable communication and manifestation abilities.",
    "My defined Root supplies consistent pressure that drives completion and transformation.",
    "My defined Solar Plexus creates emotional wisdom that deepens my decisions.",
    "I take complex, confusing aspects of life and transform them into clarity.",
    "I develop true mastery through focused attention and dedicated practice.",
    "I share my wisdom in ways that genuinely help others thrive.",
    "My unconscious design processes past experiences into valuable wisdom.",
    "My conscious personality expresses expertise with passionate enthusiasm.",
    "The world needs my distinctive combination of mental depth and intuitive wisdom."
];

// Gate Information for Modal
const gateInfo = {
    64: {
        title: "Gate 64 - Confusion / Before Completion",
        description: "Located in the Head Center, this gate creates mental pressure to transform chaotic information into breakthrough insights. You're designed to sit with confusion until clarity emerges naturally. This is not a weakness but a superpower - the ability to process complexity into wisdom.",
        gift: "Your gift is taking the confusing and making it comprehensible. Trust the process of mental pressure leading to sudden breakthroughs.",
        mantra: "I transform confusion into clarity through patient processing."
    },
    63: {
        title: "Gate 63 - Doubt / After Completion",
        description: "Located in the Head Center, this gate brings healthy skepticism and logical questioning. You're designed to doubt and question assumptions until they prove themselves logically sound. This critical thinking protects you and others from false beliefs.",
        gift: "Your gift is seeing through assumptions to find what's actually true. Your skepticism is valuable wisdom.",
        mantra: "I question wisely and accept only what proves itself logically."
    },
    9: {
        title: "Gate 9 - Focus / Taming Power of Small",
        description: "Located in the Sacral Center, this gate gives you the ability to concentrate intensely on details and perfect skills through focused repetition. You can zoom in on minutiae and develop true mastery through dedicated attention.",
        gift: "Your gift is developing deep expertise through concentrated focus. You master what others merely dabble in.",
        mantra: "I focus intensely and develop mastery through dedicated attention."
    },
    16: {
        title: "Gate 16 - Skills / Enthusiasm",
        description: "Located in the Throat Center, this gate allows you to express your developed expertise with genuine enthusiasm and passion. When you've mastered something through Gate 9's focus, Gate 16 helps you share it in inspiring ways.",
        gift: "Your gift is expressing mastery with infectious enthusiasm that inspires others to develop their own skills.",
        mantra: "I share my expertise with passionate enthusiasm that uplifts others."
    }
};

// Center Information for Cards
const centerInfo = {
    sacral: {
        title: "Sacral Center - Your Life Force",
        description: "Your defined Sacral center is your powerhouse of sustainable creative and work energy. This is the most consistent and reliable part of your design. Your sacral responds with 'uh-huh' (yes) or 'uh-uh' (no) sounds that indicate what's correct for you. When you honor these gut responses and do work that genuinely lights you up, you have limitless energy. When you force yourself into things your sacral hasn't responded to, you experience frustration and burnout.",
        practice: "Practice listening for your sacral sounds in response to yes/no questions. Notice what genuinely excites this center versus what your mind thinks you 'should' do."
    },
    throat: {
        title: "Throat Center - Your Manifestation",
        description: "Your defined Throat center gives you consistent ability to manifest and express yourself. This is a motor connection that allows you to speak things into being. Unlike undefined throat centers who wait to be invited to speak, your defined throat can communicate reliably. Combined with your Manifesting Generator energy, this makes you a powerful force for bringing ideas into reality through expression.",
        practice: "Notice how speaking about your plans and intentions helps them manifest. Use your voice to create your reality."
    },
    root: {
        title: "Root Center - Your Adrenaline Drive",
        description: "Your defined Root center provides consistent pressure and drive to get things done, evolve, and transform. This pressure is healthy and sustainable for you (unlike those with undefined roots who feel overwhelmed by it). Your Root keeps you moving forward, completing cycles, and pushing through when needed. This is your get-it-done energy.",
        practice: "Honor the pressure you feel to complete things. This drive is yours to use productively, not something to resist."
    },
    emotion: {
        title: "Solar Plexus - Your Emotional Authority",
        description: "Your defined Solar Plexus creates your Emotional Authority - the most sophisticated decision-making system in Human Design. You experience emotional waves from high to low, and MUST ride these waves before making important decisions. There is literally no truth in the now for you. What feels right at emotional highs may feel wrong at lows. True clarity emerges when you can feel the same about something at different points in your wave - often taking days or weeks.",
        practice: "For big decisions, commit to waiting through at least one full emotional cycle. Notice how your feelings about the decision shift over time. True clarity feels neutral - neither high nor low, just clear."
    }
};

// Initialize particles background
function initParticles() {
    const container = document.getElementById('particlesContainer');
    // Particles are handled by CSS, but we can add more dynamic particles here if needed
}

// Affirmation functionality
let currentAffirmationIndex = -1;
let usedAffirmations = [];

function getNewAffirmation() {
    // If we've used all affirmations, reset
    if (usedAffirmations.length === affirmations.length) {
        usedAffirmations = [];
    }

    // Get unused affirmations
    const availableAffirmations = affirmations.filter((_, index) => !usedAffirmations.includes(index));

    // Select random from available
    const randomIndex = Math.floor(Math.random() * availableAffirmations.length);
    const affirmation = availableAffirmations[randomIndex];

    // Mark as used
    const originalIndex = affirmations.indexOf(affirmation);
    usedAffirmations.push(originalIndex);

    return affirmation;
}

function showAffirmation() {
    const affirmationText = document.getElementById('affirmationText');
    const newAffirmation = getNewAffirmation();

    // Fade out
    affirmationText.style.opacity = '0';

    setTimeout(() => {
        affirmationText.textContent = newAffirmation;
        // Fade in
        affirmationText.style.opacity = '1';
    }, 300);
}

// Gate card click handlers
function showGateInfo(gateNumber) {
    const modal = document.getElementById('gateModal');
    const modalTitle = document.getElementById('modalTitle');
    const modalBody = document.getElementById('modalBody');

    const gate = gateInfo[gateNumber];

    modalTitle.textContent = gate.title;
    modalBody.innerHTML = `
        <p><strong>Description:</strong></p>
        <p>${gate.description}</p>
        <br>
        <p><strong>Your Gift:</strong></p>
        <p>${gate.gift}</p>
        <br>
        <p><strong>Personal Mantra:</strong></p>
        <p style="font-style: italic; color: var(--emotion-purple); text-align: center; font-size: 1.2rem; margin-top: 1rem;">
            "${gate.mantra}"
        </p>
    `;

    modal.classList.add('active');
}

// Center card click handlers
function showCenterInfo(centerName) {
    const modal = document.getElementById('gateModal');
    const modalTitle = document.getElementById('modalTitle');
    const modalBody = document.getElementById('modalBody');

    const center = centerInfo[centerName];

    modalTitle.textContent = center.title;
    modalBody.innerHTML = `
        <p>${center.description}</p>
        <br>
        <p><strong>Practice:</strong></p>
        <p style="font-style: italic; color: var(--emotion-purple);">${center.practice}</p>
    `;

    modal.classList.add('active');
}

// Close modal
function closeModal() {
    const modal = document.getElementById('gateModal');
    modal.classList.remove('active');
}

// Download as PDF functionality (simplified - directs to browser print)
function downloadPDF() {
    // Trigger browser print dialog which allows "Save as PDF"
    window.print();
}

// Scroll animations
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe all sections with animate class
    document.querySelectorAll('.animate-slide-in').forEach(section => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(30px)';
        section.style.transition = 'opacity 0.8s ease, transform 0.8s ease';
        observer.observe(section);
    });
}

// Initialize emotional wave animation
function initEmotionalWave() {
    // The wave animation is handled by CSS
    // This function can be extended for more complex animations
    console.log('Emotional wave visualization active');
}

// Add floating animation to commitment cards
function initCommitmentAnimations() {
    const cards = document.querySelectorAll('.commitment-card');

    cards.forEach((card, index) => {
        // Stagger the animations
        card.style.animationDelay = `${index * 0.1}s`;
    });
}

// Log welcome message
function logWelcomeMessage() {
    console.log('%c🌟 Welcome to Your Emotional Manifesto 🌟', 'font-size: 20px; font-weight: bold; color: #764ba2;');
    console.log('%cYou are a 5/1 Manifesting Generator with Emotional Authority', 'font-size: 14px; color: #4ECDC4;');
    console.log('%cYour life purpose: Master Synthesizer', 'font-size: 14px; color: #FF6B35;');
    console.log('%c✨ Trust your processes, honor your rhythms, share your gifts ✨', 'font-size: 12px; font-style: italic; color: #667eea;');
}

// Get daily affirmation based on date (so it's consistent for the day)
function getDailyAffirmation() {
    const today = new Date();
    const dayOfYear = Math.floor((today - new Date(today.getFullYear(), 0, 0)) / 1000 / 60 / 60 / 24);
    const index = dayOfYear % affirmations.length;
    return affirmations[index];
}

// Initialize everything when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    // Initialize particles
    initParticles();

    // Initialize scroll animations
    initScrollAnimations();

    // Initialize emotional wave
    initEmotionalWave();

    // Initialize commitment animations
    initCommitmentAnimations();

    // Set up affirmation button
    const affirmationBtn = document.getElementById('newAffirmationBtn');
    const affirmationText = document.getElementById('affirmationText');

    // Show daily affirmation on first load
    affirmationText.textContent = getDailyAffirmation();

    affirmationBtn.addEventListener('click', showAffirmation);

    // Set up gate card clicks
    document.querySelectorAll('.gate-card').forEach(card => {
        card.addEventListener('click', () => {
            const gateNumber = parseInt(card.dataset.gate);
            showGateInfo(gateNumber);
        });
    });

    // Set up center card clicks
    document.querySelectorAll('.identity-card').forEach(card => {
        card.addEventListener('click', () => {
            const centerName = card.dataset.center;
            if (centerName && centerInfo[centerName]) {
                showCenterInfo(centerName);
            }
        });
    });

    // Set up modal close
    const closeModalBtn = document.getElementById('closeModal');
    const modal = document.getElementById('gateModal');

    closeModalBtn.addEventListener('click', closeModal);

    // Close modal when clicking outside
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeModal();
        }
    });

    // Close modal with Escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('active')) {
            closeModal();
        }
    });

    // Set up download button
    const downloadBtn = document.getElementById('downloadBtn');
    downloadBtn.addEventListener('click', downloadPDF);

    // Log welcome message
    logWelcomeMessage();

    // Add smooth scroll behavior
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // Console easter egg - show all affirmations
    window.showAllAffirmations = () => {
        console.log('%c📿 All 50 Affirmations for Your Design 📿', 'font-size: 16px; font-weight: bold; color: #764ba2;');
        affirmations.forEach((affirmation, index) => {
            console.log(`%c${index + 1}. ${affirmation}`, 'color: #4ECDC4;');
        });
    };

    // Console hint
    console.log('%c💡 Tip: Type showAllAffirmations() to see all 50 affirmations!', 'font-style: italic; color: #b8b8b8;');
});

// Add window resize handler for responsive adjustments
window.addEventListener('resize', () => {
    // Handle any resize-specific logic here
});

// Log when page is fully loaded
window.addEventListener('load', () => {
    console.log('%c✅ Manifesto fully loaded and ready', 'color: #44A08D; font-weight: bold;');
});
