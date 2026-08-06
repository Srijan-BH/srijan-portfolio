/* ==========================================================================
   SRIJAN B H PORTFOLIO - INTERACTIVE JAVASCRIPT LOGIC
   Canvas Particles | Typing Effect | Navigation Scrollspy | Modals | Forms
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
    
    // ----------------------------------------------------------------------
    // 01. INTERACTIVE HTML5 CANVAS PARTICLE BACKDROP
    // ----------------------------------------------------------------------
    const initCanvasParticles = () => {
        const canvas = document.getElementById('bg-canvas');
        if (!canvas) return;

        const ctx = canvas.getContext('2d');
        let width = canvas.width = window.innerWidth;
        let height = canvas.height = window.innerHeight;

        let particles = [];
        // Optimize for mobile: fewer particles based on screen width
        const particleCount = window.innerWidth < 768 ? Math.floor(window.innerWidth / 25) : Math.min(Math.floor(window.innerWidth / 16), 85);
        
        let mouse = {
            x: null,
            y: null,
            radius: 140
        };

        window.addEventListener('mousemove', (e) => {
            mouse.x = e.clientX;
            mouse.y = e.clientY;
        });

        window.addEventListener('mouseleave', () => {
            mouse.x = null;
            mouse.y = null;
        });

        window.addEventListener('resize', () => {
            width = canvas.width = window.innerWidth;
            height = canvas.height = window.innerHeight;
        });

        class Particle {
            constructor() {
                this.x = Math.random() * width;
                this.y = Math.random() * height;
                this.vx = (Math.random() - 0.5) * 0.8;
                this.vy = (Math.random() - 0.5) * 0.8;
                this.radius = Math.random() * 2 + 1;
                this.color = Math.random() > 0.5 ? 'rgba(0, 242, 254, ' : 'rgba(168, 85, 247, ';
                this.alpha = Math.random() * 0.5 + 0.2;
            }

            draw() {
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
                ctx.fillStyle = this.color + this.alpha + ')';
                ctx.shadowBlur = 10;
                ctx.shadowColor = this.color + '0.8)';
                ctx.fill();
                ctx.shadowBlur = 0;
            }

            update() {
                this.x += this.vx;
                this.y += this.vy;

                // Bounce off edges
                if (this.x < 0 || this.x > width) this.vx *= -1;
                if (this.y < 0 || this.y > height) this.vy *= -1;

                // Mouse interaction
                if (mouse.x && mouse.y) {
                    const dx = mouse.x - this.x;
                    const dy = mouse.y - this.y;
                    const distance = Math.sqrt(dx * dx + dy * dy);
                    if (distance < mouse.radius) {
                        const force = (mouse.radius - distance) / mouse.radius;
                        this.x -= (dx / distance) * force * 3;
                        this.y -= (dy / distance) * force * 3;
                    }
                }

                this.draw();
            }
        }

        for (let i = 0; i < particleCount; i++) {
            particles.push(new Particle());
        }

        const connectParticles = () => {
            for (let a = 0; a < particles.length; a++) {
                for (let b = a + 1; b < particles.length; b++) {
                    const dx = particles[a].x - particles[b].x;
                    const dy = particles[a].y - particles[b].y;
                    const distance = Math.sqrt(dx * dx + dy * dy);

                    if (distance < 120) {
                        const opacity = 1 - (distance / 120);
                        ctx.strokeStyle = `rgba(0, 242, 254, ${opacity * 0.18})`;
                        ctx.lineWidth = 0.8;
                        ctx.beginPath();
                        ctx.moveTo(particles[a].x, particles[a].y);
                        ctx.lineTo(particles[b].x, particles[b].y);
                        ctx.stroke();
                    }
                }
            }
        };

        const animate = () => {
            ctx.clearRect(0, 0, width, height);
            particles.forEach(p => p.update());
            connectParticles();
            requestAnimationFrame(animate);
        };

        animate();
    };

    initCanvasParticles();

    // ----------------------------------------------------------------------
    // 02. HERO SECTION DYNAMIC TYPING EFFECT
    // ----------------------------------------------------------------------
    const initTypingEffect = () => {
        const targetElement = document.getElementById('hero-typing');
        if (!targetElement) return;

        const roles = [
            "Full Stack Developer",
            "MERN Stack Specialist",
            "Docker & K8s Developer",
            "MCA Student",
            "Python/Flask Developer",
            "AI/ML Enthusiast"
        ];

        let roleIndex = 0;
        let charIndex = 0;
        let isDeleting = false;
        let typingSpeed = 100;

        const type = () => {
            const currentRole = roles[roleIndex];

            if (isDeleting) {
                targetElement.textContent = currentRole.substring(0, charIndex - 1);
                charIndex--;
                typingSpeed = 50;
            } else {
                targetElement.textContent = currentRole.substring(0, charIndex + 1);
                charIndex++;
                typingSpeed = 100;
            }

            if (!isDeleting && charIndex === currentRole.length) {
                isDeleting = true;
                typingSpeed = 2000; // Pause at full word
            } else if (isDeleting && charIndex === 0) {
                isDeleting = false;
                roleIndex = (roleIndex + 1) % roles.length;
                typingSpeed = 500; // Pause before typing next word
            }

            setTimeout(type, typingSpeed);
        };

        type();
    };

    initTypingEffect();

    // ----------------------------------------------------------------------
    // 03. NAVBAR SCROLL SPY & STICKY STYLING
    // ----------------------------------------------------------------------
    const navbar = document.getElementById('navbar');
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('section');
    const backToTopBtn = document.getElementById('back-to-top');
    const progressBar = document.getElementById('scroll-progress-bar');

    const handleScroll = () => {
        const scrollY = window.scrollY;

        // Scroll Progress Bar Update
        if (progressBar) {
            const docHeight = document.documentElement.scrollHeight - window.innerHeight;
            const scrollPercent = (scrollY / docHeight) * 100;
            progressBar.style.width = `${scrollPercent}%`;
        }

        // Sticky Navbar Toggle
        if (scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }

        // Back to Top Button Toggle
        if (scrollY > 500) {
            backToTopBtn?.classList.add('show');
        } else {
            backToTopBtn?.classList.remove('show');
        }

        // Active Section Scrollspy
        let currentSectionId = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 120;
            const sectionHeight = section.offsetHeight;
            if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
                currentSectionId = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${currentSectionId}`) {
                link.classList.add('active');
            }
        });
    };

    window.addEventListener('scroll', handleScroll);

    backToTopBtn?.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    // ----------------------------------------------------------------------
    // 04. MOBILE HAMBURGER MENU TOGGLE
    // ----------------------------------------------------------------------
    const hamburger = document.getElementById('hamburger');
    const navMenu = document.getElementById('nav-menu');

    if (hamburger && navMenu) {
        hamburger.addEventListener('click', () => {
            const isActive = hamburger.classList.toggle('active');
            navMenu.classList.toggle('active');
            
            // Lock body scroll on mobile
            if (isActive) {
                document.body.style.overflow = 'hidden';
            } else {
                document.body.style.overflow = '';
            }
        });

        // Close menu on link click
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                hamburger.classList.remove('active');
                navMenu.classList.remove('active');
                document.body.style.overflow = '';
            });
        });
    }

    // ----------------------------------------------------------------------
    // 05. SKILLS FILTERING TABS
    // ----------------------------------------------------------------------
    const filterButtons = document.querySelectorAll('#skill-filters .filter-btn');
    const skillCards = document.querySelectorAll('#skills-grid .skill-card');

    filterButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            filterButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filterValue = btn.getAttribute('data-filter');

            skillCards.forEach(card => {
                const categories = card.getAttribute('data-category');
                if (filterValue === 'all' || categories.includes(filterValue)) {
                    card.style.display = 'block';
                    card.style.opacity = '1';
                } else {
                    card.style.display = 'none';
                    card.style.opacity = '0';
                }
            });
        });
    });

    // ----------------------------------------------------------------------
    // 06. PROJECT TECHNICAL SPECS MODAL
    // ----------------------------------------------------------------------
    const modalOverlay = document.getElementById('project-modal');
    const modalContent = document.getElementById('modal-content');
    const modalClose = document.getElementById('modal-close');
    const viewDetailsBtns = document.querySelectorAll('.view-details-btn');

    const projectData = {
        airguard: {
            title: "AirGuard AI – Predictive Air Quality Monitoring System",
            category: "Full Stack & Environmental AI",
            overview: "A state-of-the-art environmental web application engineered to monitor and analyze global Air Quality Index (AQI) data in real time.",
            features: [
                "Real-time AQI tracking powered by OpenWeather API integration.",
                "Leaflet.js interactive geospatial map visualizing pollution hotspots globally.",
                "Emergency response dispatcher built with Flask backend and Twilio mass SMS gateway.",
                "Integrated Web Speech API assistant for voice-activated voice search and query response."
            ],
            techStack: ["JavaScript (ES6+)", "Python (Flask)", "MongoDB", "Twilio API", "OpenWeather API", "Leaflet.js", "Web Speech API"],
            liveUrl: "https://airguard-system.netlify.app",
            githubUrl: "https://github.com/Srijan-BH"
        },
        ngo: {
            title: "NGO Volunteer Management System",
            category: "Full Stack & WebSockets Platform",
            overview: "An enterprise-grade volunteer management platform designed for non-profit organizations to handle volunteer onboarding, event creation, and spatial mapping.",
            features: [
                "Mapbox API integration for interactive location-based volunteer event mapping.",
                "Real-time instant community chat powered by Flask-SocketIO WebSockets.",
                "Role-based access control with secure JSON Web Token (JWT) authentication.",
                "MongoDB Atlas cloud cluster storing structured volunteer profiles, hours, and event metrics."
            ],
            techStack: ["Python (Flask)", "MongoDB Atlas", "Flask-SocketIO", "WebSockets", "Mapbox API", "JavaScript", "JWT Auth"],
            liveUrl: "https://ngo-volunteer-system-x469.onrender.com",
            githubUrl: "https://github.com/Srijan-BH"
        }
    };

    // ----------------------------------------------------------------------
    // 06B. 3D CARD TILT EFFECT ON MOUSEMOVE
    // ----------------------------------------------------------------------
    const tiltCards = document.querySelectorAll('.tilt-card');
    tiltCards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            
            const rotateX = ((y - centerY) / centerY) * -8;
            const rotateY = ((x - centerX) / centerX) * 8;
            
            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-6px)`;
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0px)';
        });
    });

    viewDetailsBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const key = btn.getAttribute('data-project');
            const data = projectData[key];
            if (!data) return;

            modalContent.innerHTML = `
                <span class="badge badge-cyan" style="margin-bottom: 0.5rem;">${data.category}</span>
                <h2 style="font-family: var(--font-heading); font-size: 1.5rem; margin-bottom: 1rem;">${data.title}</h2>
                <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1.25rem;">${data.overview}</p>

                <h4 style="color: var(--cyan-neon); font-size: 0.95rem; margin-bottom: 0.5rem;">Key Architecture Features:</h4>
                <ul style="list-style: disc; padding-left: 1.2rem; color: var(--text-muted); font-size: 0.88rem; margin-bottom: 1.5rem;">
                    ${data.features.map(f => `<li style="margin-bottom: 0.3rem;">${f}</li>`).join('')}
                </ul>

                <h4 style="color: var(--cyan-neon); font-size: 0.95rem; margin-bottom: 0.5rem;">Technologies Used:</h4>
                <div style="display: flex; flex-wrap: wrap; gap: 0.4rem; margin-bottom: 1.5rem;">
                    ${data.techStack.map(t => `<span class="tech-tag">${t}</span>`).join('')}
                </div>

                <div style="display: flex; gap: 1rem; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 1rem;">
                    <a href="${data.liveUrl}" target="_blank" class="btn btn-primary btn-sm"><i class="fa-solid fa-arrow-up-right-from-square"></i> Open Live App</a>
                    <a href="${data.githubUrl}" target="_blank" class="btn btn-outline btn-sm"><i class="fa-brands fa-github"></i> Source Code</a>
                </div>
            `;

            modalOverlay.classList.add('active');
            modalOverlay.setAttribute('aria-hidden', 'false');
        });
    });

    modalClose?.addEventListener('click', () => {
        modalOverlay.classList.remove('active');
        modalOverlay.setAttribute('aria-hidden', 'true');
    });

    modalOverlay?.addEventListener('click', (e) => {
        if (e.target === modalOverlay) {
            modalOverlay.classList.remove('active');
            modalOverlay.setAttribute('aria-hidden', 'true');
        }
    });

    // ----------------------------------------------------------------------
    // 07. CONTACT FORM VALIDATION & TOAST NOTIFICATION
    // ----------------------------------------------------------------------
    const contactForm = document.getElementById('contact-form');
    const toast = document.getElementById('toast');

    const showToast = (message) => {
        if (!toast) return;
        toast.textContent = message;
        toast.classList.add('show');
        setTimeout(() => {
            toast.classList.remove('show');
        }, 4500);
    };

    if (contactForm) {
        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            const submitBtn = document.getElementById('submit-btn');
            const nameVal = document.getElementById('name').value.trim();
            const emailVal = document.getElementById('email').value.trim();

            if (!nameVal || !emailVal) {
                showToast('Please complete all required form fields.');
                return;
            }

            // Show loading state
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<i class="fa-solid fa-circle-notch fa-spin"></i> Sending...';
            }

            try {
                const formData = new FormData(contactForm);
                const response = await fetch(contactForm.action, {
                    method: 'POST',
                    body: formData,
                    headers: { 'Accept': 'application/json' }
                });

                if (response.ok) {
                    showToast(`✅ Message sent! Srijan will get back to you soon.`);
                    contactForm.reset();
                } else {
                    const data = await response.json();
                    const errMsg = data?.errors?.map(e => e.message).join(', ') || 'Something went wrong.';
                    showToast(`❌ Error: ${errMsg}`);
                }
            } catch (err) {
                showToast('❌ Network error. Please try emailing directly at srijannaik355@gmail.com');
            } finally {
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = '<i class="fa-solid fa-paper-plane"></i> Send Message';
                }
            }
        });
    }

    // ----------------------------------------------------------------------
    // 08. ADVANCED PRELOADER & PAGE TRANSITIONS
    // ----------------------------------------------------------------------
    const preloader = document.getElementById('preloader');
    const typedText = document.getElementById('preloader-typed');
    const barFill = document.getElementById('preloader-bar-fill');
    const pageTransition = document.getElementById('page-transition');

    const textToType = "Srijan.dev";
    let typeIndex = 0;
    let typeInterval;

    const hidePreloader = () => {
        if (preloader && !preloader.classList.contains('hidden')) {
            preloader.classList.add('hidden');
        }
    };

    const runPreloader = () => {
        // Typing animation
        typeInterval = setInterval(() => {
            if (typeIndex < textToType.length) {
                typedText.textContent += textToType.charAt(typeIndex);
                typeIndex++;
            } else {
                clearInterval(typeInterval);
                setTimeout(hidePreloader, 400); // Hide shortly after finishing typing
            }
        }, 120); // Typing speed

        // Progress bar animation
        if(barFill) {
            let progress = 0;
            const progressInterval = setInterval(() => {
                progress += Math.random() * 15;
                if(progress > 100) progress = 100;
                barFill.style.width = `${progress}%`;
                if(progress === 100) clearInterval(progressInterval);
            }, 100);
        }
    };

    if (document.readyState === 'complete') {
        runPreloader();
    } else {
        window.addEventListener('load', runPreloader);
        // Fallback
        setTimeout(runPreloader, 500);
    }

    // Page Transition effect for links
    document.querySelectorAll('a').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            
            // Only apply transition if it's an external link or navigating to another page
            if (href && !href.startsWith('#') && !href.startsWith('mailto:') && !this.hasAttribute('download') && this.getAttribute('target') !== '_blank') {
                e.preventDefault();
                if(pageTransition) {
                    pageTransition.classList.add('active');
                    setTimeout(() => {
                        window.location = href;
                    }, 400); // Match CSS transition time
                } else {
                    window.location = href;
                }
            }
        });
    });

    // ----------------------------------------------------------------------
    // 09. DARK / LIGHT THEME TOGGLE
    // ----------------------------------------------------------------------
    const themeToggle = document.getElementById('theme-toggle');
    const themeIcon = document.getElementById('theme-icon');
    const savedTheme = localStorage.getItem('srijan_theme');

    if (savedTheme === 'light') {
        document.documentElement.setAttribute('data-theme', 'light');
        if (themeIcon) {
            themeIcon.className = 'fa-solid fa-sun';
        }
    }

    themeToggle?.addEventListener('click', () => {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        if (currentTheme === 'light') {
            document.documentElement.removeAttribute('data-theme');
            localStorage.setItem('srijan_theme', 'dark');
            if (themeIcon) themeIcon.className = 'fa-solid fa-moon';
        } else {
            document.documentElement.setAttribute('data-theme', 'light');
            localStorage.setItem('srijan_theme', 'light');
            if (themeIcon) themeIcon.className = 'fa-solid fa-sun';
        }
    });

    // ----------------------------------------------------------------------
    // 10. ANIMATED STATISTICS COUNTER & SCROLL REVEAL
    // ----------------------------------------------------------------------
    const initScrollRevealAndCounters = () => {
        // Scroll Reveal Elements
        const revealElements = document.querySelectorAll('.scroll-reveal');
        
        const revealObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('revealed');
                }
            });
        }, { threshold: 0.15 });

        revealElements.forEach(el => revealObserver.observe(el));

        // Animated Statistics Counter
        const statsBar = document.getElementById('stats-counter-bar');
        const statNumbers = document.querySelectorAll('.stat-number[data-target]');
        let countStarted = false;

        const startCounting = () => {
            statNumbers.forEach(stat => {
                const target = parseInt(stat.getAttribute('data-target'), 10);
                const duration = 2000;
                const stepTime = 50;
                const steps = duration / stepTime;
                const increment = target / steps;
                let current = 0;

                const timer = setInterval(() => {
                    current += increment;
                    if (current >= target) {
                        stat.textContent = target + '+';
                        clearInterval(timer);
                    } else {
                        stat.textContent = Math.ceil(current);
                    }
                }, stepTime);
            });
        };

        if (statsBar) {
            const statsObserver = new IntersectionObserver((entries) => {
                if (entries[0].isIntersecting && !countStarted) {
                    countStarted = true;
                    startCounting();
                }
            }, { threshold: 0.3 });

            statsObserver.observe(statsBar);
        }
    };

    initScrollRevealAndCounters();

    // ----------------------------------------------------------------------
    // 11. CUSTOM CURSOR & TRAIL EFFECT
    // ----------------------------------------------------------------------
    const cursorDot = document.querySelector('[data-cursor-dot]');
    const cursorOutline = document.querySelector('[data-cursor-outline]');

    if (cursorDot && cursorOutline && window.matchMedia("(pointer: fine)").matches) {
        
        // Create Trail Elements
        const trails = [];
        const numTrails = 12;
        for (let i = 0; i < numTrails; i++) {
            const trail = document.createElement('div');
            trail.className = 'cursor-trail';
            document.body.appendChild(trail);
            trails.push({ el: trail, x: window.innerWidth/2, y: window.innerHeight/2 });
        }

        let mouseX = window.innerWidth / 2;
        let mouseY = window.innerHeight / 2;

        window.addEventListener('mousemove', (e) => {
            mouseX = e.clientX;
            mouseY = e.clientY;

            // Direct Dot Movement
            cursorDot.style.left = `${mouseX}px`;
            cursorDot.style.top = `${mouseY}px`;
            cursorDot.style.opacity = 1;
            cursorOutline.style.opacity = 1;
            trails.forEach(t => t.el.style.opacity = 1);
            
            // Outline Movement with slight delay
            cursorOutline.animate({
                left: `${mouseX}px`,
                top: `${mouseY}px`
            }, { duration: 150, fill: "forwards" });
        });

        // Trail Animation Loop (Spring Physics)
        const animateTrails = () => {
            let x = mouseX;
            let y = mouseY;

            trails.forEach((trail, index) => {
                // Follow the previous trail position
                trail.x += (x - trail.x) * 0.4;
                trail.y += (y - trail.y) * 0.4;
                
                trail.el.style.left = `${trail.x}px`;
                trail.el.style.top = `${trail.y}px`;
                
                // Scale down based on index for a comet tail effect
                const scale = (numTrails - index) / numTrails;
                trail.el.style.transform = `translate(-50%, -50%) scale(${scale})`;
                
                x = trail.x;
                y = trail.y;
            });

            requestAnimationFrame(animateTrails);
        };
        animateTrails();

        // Hover effect for interactive elements
        const interactiveElements = document.querySelectorAll('a, button, input, textarea, .skill-card, .project-card, .theme-toggle');
        
        interactiveElements.forEach(el => {
            el.addEventListener('mouseenter', () => {
                cursorOutline.classList.add('hover');
                cursorDot.style.transform = 'translate(-50%, -50%) scale(0.5)';
                trails.forEach(t => t.el.style.opacity = 0); // Hide trails on hover for cleaner look
            });
            el.addEventListener('mouseleave', () => {
                cursorOutline.classList.remove('hover');
                cursorDot.style.transform = 'translate(-50%, -50%) scale(1)';
                trails.forEach(t => t.el.style.opacity = 1);
            });
        });

        // Hide cursor when leaving window
        document.addEventListener('mouseleave', () => {
            cursorDot.style.opacity = 0;
            cursorOutline.style.opacity = 0;
            trails.forEach(t => t.el.style.opacity = 0);
        });
        
        document.addEventListener('mouseenter', () => {
            cursorDot.style.opacity = 1;
            cursorOutline.style.opacity = 1;
            trails.forEach(t => t.el.style.opacity = 1);
        });
    }

    // Update dynamic footer year
    const yearSpan = document.getElementById('current-year');
    if (yearSpan) {
        yearSpan.textContent = new Date().getFullYear();
    }
});
