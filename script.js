// Day of the Dead 16th Birthday Card - Interactive Script

// Memory Data for each year (customize these!)
const memories = {
    1: {
        title: "Year 1 - First Steps 👶",
        content: "Your first year brought so much joy! You learned to walk, talk, and fill our lives with laughter. Every day was a new adventure."
    },
    2: {
        title: "Year 2 - Curious Explorer 🧸",
        content: "At two, you became a little explorer! Everything was fascinating to you. Your curiosity knew no bounds."
    },
    3: {
        title: "Year 3 - Preschool Days 🎨",
        content: "Your first days of preschool! You made friends, painted masterpieces, and showed everyone your brilliant smile."
    },
    4: {
        title: "Year 4 - Dinosaur Phase 🦕",
        content: "The year of dinosaurs! You could name every species and loved acting like a T-Rex. Roar!"
    },
    5: {
        title: "Year 5 - Big Kid School 📚",
        content: "Starting elementary school! You were so excited with your new backpack and ready to learn everything."
    },
    6: {
        title: "Year 6 - Sports Star ⚽",
        content: "You discovered sports this year! Whether soccer, basketball, or just running around, you had endless energy."
    },
    7: {
        title: "Year 7 - Creative Genius 🎭",
        content: "Your creativity flourished! From art projects to imaginative stories, you showed your unique perspective."
    },
    8: {
        title: "Year 8 - Tech Wizard 💻",
        content: "Technology became your passion! You started learning to code and build amazing things."
    },
    9: {
        title: "Year 9 - Adventure Year 🏕️",
        content: "So many adventures! Camping trips, new experiences, and making unforgettable memories."
    },
    10: {
        title: "Year 10 - Double Digits! 🎉",
        content: "A milestone year! You reached double digits and became more independent and confident."
    },
    11: {
        title: "Year 11 - Middle School 📖",
        content: "Middle school brought new challenges and friendships. You handled it all with grace and determination."
    },
    12: {
        title: "Year 12 - Musical Moments 🎵",
        content: "Music filled your life this year! Whether listening or creating, you found your rhythm."
    },
    13: {
        title: "Year 13 - Teenager! 😎",
        content: "Officially a teenager! You started finding your own style and voice in the world."
    },
    14: {
        title: "Year 14 - Growth Spurt 📏",
        content: "You grew so much this year - not just physically, but in wisdom and maturity too!"
    },
    15: {
        title: "Year 15 - Quinceañero 🎊",
        content: "Last year's milestone! You've grown into an amazing young person with so much potential."
    },
    16: {
        title: "Year 16 - Sweet Sixteen! 🎂",
        content: "And here we are! Sixteen years of love, laughter, and incredible memories. Born on Día de los Muertos, you've always been special. Here's to celebrating life, honoring our ancestors, and looking forward to all the amazing things ahead. ¡Feliz cumpleaños, mijo! 💀🎉✨"
    }
};

// Track clicked petals
let clickedPetals = new Set();
let secretClicks = 0;
const konamiCode = [];
const konamiSequence = ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'b', 'a'];

// Initialize falling petals
function createFallingPetals() {
    const container = document.getElementById('petalsContainer');
    const petals = ['🌼', '🌺', '🌸', '🌻', '🏵️', '💐'];

    setInterval(() => {
        const petal = document.createElement('div');
        petal.className = 'petal-fall';
        petal.textContent = petals[Math.floor(Math.random() * petals.length)];
        petal.style.left = Math.random() * 100 + '%';
        petal.style.animationDuration = (Math.random() * 3 + 5) + 's';
        petal.style.animationDelay = Math.random() * 2 + 's';
        container.appendChild(petal);

        // Remove petal after animation
        setTimeout(() => {
            petal.remove();
        }, 8000);
    }, 500);
}

// Confetti effect
function launchConfetti() {
    const canvas = document.getElementById('confettiCanvas');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const confetti = [];
    const colors = ['#FFA500', '#9D4EDD', '#FF006E', '#06FFA5', '#FFD60A'];

    for (let i = 0; i < 150; i++) {
        confetti.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height - canvas.height,
            size: Math.random() * 10 + 5,
            speedY: Math.random() * 3 + 2,
            speedX: Math.random() * 3 - 1.5,
            color: colors[Math.floor(Math.random() * colors.length)],
            rotation: Math.random() * 360,
            rotationSpeed: Math.random() * 10 - 5
        });
    }

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        confetti.forEach((piece, index) => {
            ctx.save();
            ctx.translate(piece.x, piece.y);
            ctx.rotate(piece.rotation * Math.PI / 180);
            ctx.fillStyle = piece.color;
            ctx.fillRect(-piece.size / 2, -piece.size / 2, piece.size, piece.size);
            ctx.restore();

            piece.y += piece.speedY;
            piece.x += piece.speedX;
            piece.rotation += piece.rotationSpeed;

            if (piece.y > canvas.height) {
                confetti.splice(index, 1);
            }
        });

        if (confetti.length > 0) {
            requestAnimationFrame(animate);
        } else {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
        }
    }

    animate();
}

// Play click sound
function playClickSound() {
    const sound = document.getElementById('clickSound');
    sound.currentTime = 0;
    sound.play().catch(() => {
        // Ignore if sound doesn't play
    });
}

// Show memory modal
function showMemory(year) {
    const modal = document.getElementById('memoryModal');
    const title = document.getElementById('modalTitle');
    const body = document.getElementById('modalBody');

    const memory = memories[year];
    title.textContent = memory.title;
    body.innerHTML = `<p>${memory.content}</p>`;

    modal.style.display = 'block';
    launchConfetti();
    playClickSound();
}

// Close modal
function closeModal() {
    const modal = document.getElementById('memoryModal');
    modal.style.display = 'none';
}

// Handle petal clicks
function handlePetalClick(event) {
    const petal = event.currentTarget;
    const year = parseInt(petal.dataset.year);

    clickedPetals.add(year);
    petal.classList.add('clicked');

    showMemory(year);

    // Check if all petals clicked
    if (clickedPetals.size === 16) {
        setTimeout(() => {
            alert('🎉 ¡Increíble! You\'ve unlocked all 16 memories! You truly are special. 💀✨');
            launchConfetti();
        }, 500);
    }
}

// Handle skull click
function handleSkullClick() {
    secretClicks++;

    const messages = [
        "💀 The skull smiles at you!",
        "🌺 You're one year closer to being able to vote!",
        "🎉 Sixteen candles, one amazing person!",
        "✨ Born on Día de los Muertos - you're destined for greatness!",
        "🌼 Keep clicking... there might be a surprise!",
        "🎊 Your ancestors are proud of you!",
        "💫 Sweet 16 and never been... more awesome!",
        "🌸 Fun fact: You share your birthday with a beautiful tradition!",
        "🎨 Life is your canvas - paint it colorful!",
        "🎭 The best is yet to come!",
        "🚀 Ready to conquer the world at 16!",
        "🌟 You light up every room you enter!",
        "🎪 Life's a celebration - especially today!",
        "🎯 At 16, the world is your target!",
        "🏆 Champion of our hearts!"
    ];

    const randomMessage = messages[Math.floor(Math.random() * messages.length)];
    alert(randomMessage);

    if (secretClicks === 3) {
        launchConfetti();
        setTimeout(() => {
            alert("🎊 TRIPLE SKULL BONUS! 🎊\n\nYou've discovered the secret! Here's your special message:\n\n'You were born on a day that celebrates life by remembering those who came before. Like the marigold petals that guide spirits home, may your path always be lit with love, laughter, and the wisdom of generations. ¡Feliz cumpleaños, hijo querido! 💀🌺✨'");
        }, 100);
    }

    if (secretClicks === 16) {
        launchConfetti();
        setTimeout(() => {
            alert("🌟 ULTIMATE ACHIEVEMENT UNLOCKED! 🌟\n\n16 clicks for 16 years!\n\nYou're as persistent as you are amazing. Never lose that spirit! The world needs more people like you. 🎉💀🌈");
            // Triple confetti!
            launchConfetti();
            setTimeout(() => launchConfetti(), 500);
        }, 100);
    }
}

// Next memory button
function nextMemory() {
    const currentYear = parseInt(document.getElementById('modalTitle').textContent.match(/\d+/)[0]);
    const nextYear = currentYear === 16 ? 1 : currentYear + 1;

    // Mark current as clicked
    clickedPetals.add(currentYear);
    document.querySelector(`.petal[data-year="${currentYear}"]`).classList.add('clicked');

    // Also mark the *next* year as clicked when showing it.
    clickedPetals.add(nextYear);
    document.querySelector(`.petal[data-year="${nextYear}"]`).classList.add('clicked');

    // Show next
    showMemory(nextYear);
}

// Konami code easter egg
function handleKonamiCode(event) {
    konamiCode.push(event.key);

    if (konamiCode.length > konamiSequence.length) {
        konamiCode.shift();
    }

    if (konamiCode.join(',') === konamiSequence.join(',')) {
        konamiCode.length = 0;
        launchConfetti();
        setTimeout(() => {
            alert("🎮 KONAMI CODE ACTIVATED! 🎮\n\nGamer achievement unlocked!\n\nYou found the secret code! Just like in the best games, life has hidden surprises. Keep exploring, keep discovering, keep being awesome!\n\n↑↑↓↓←→←→BA\n\n🎯 Level 16 Complete! 🎯");
            launchConfetti();
            launchConfetti();
        }, 100);
    }
}

// Initialize everything
document.addEventListener('DOMContentLoaded', () => {
    // Create falling petals
    createFallingPetals();

    // Add petal click handlers
    document.querySelectorAll('.petal').forEach(petal => {
        petal.addEventListener('click', handlePetalClick);
    });

    // Add skull click handler
    document.getElementById('mainSkull').addEventListener('click', handleSkullClick);

    // Modal close handlers
    document.getElementById('closeModal').addEventListener('click', closeModal);
    document.getElementById('memoryModal').addEventListener('click', (e) => {
        if (e.target.id === 'memoryModal') {
            closeModal();
        }
    });

    // Next memory button
    document.getElementById('nextMemory').addEventListener('click', nextMemory);

    // Konami code listener
    document.addEventListener('keydown', handleKonamiCode);

    // Secret counter update
    const counter = document.getElementById('secretCounter');
    setInterval(() => {
        if (secretClicks > 0) {
            counter.textContent = `Skull clicks: ${secretClicks}`;
        }
    }, 1000);

    // Welcome message
    setTimeout(() => {
        launchConfetti();
    }, 1000);

    console.log('🎉 ¡Feliz Cumpleaños! 💀');
    console.log('Easter eggs hidden:');
    console.log('1. Click the skull multiple times...');
    console.log('2. Try the Konami Code (↑↑↓↓←→←→BA)');
    console.log('3. Click all 16 petals for a special message!');
});

// Responsive canvas resize
window.addEventListener('resize', () => {
    const canvas = document.getElementById('confettiCanvas');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});

// Auto-play birthday song hint
setTimeout(() => {
    console.log('🎵 Pro tip: Play "Las Mañanitas" for the full experience! 🎵');
}, 5000);
