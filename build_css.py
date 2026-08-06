import re

def build_css():
    with open('styles.backup.css', 'r', encoding='utf-8') as f:
        old_css = f.read()

    # The new CSS will be entirely Mobile-First.
    # We will preserve the variables, animations, and component visual styles,
    # but rewrite all layout-related CSS (grids, flex, margins, paddings, sizing).

    new_css = """/* ==========================================================================
   SRIJAN B H PORTFOLIO - MOBILE FIRST RESPONSIVE ARCHITECTURE
   Dark Theme | Cyan, Purple, Blue Neon Gradients | Strict Mobile First
   ========================================================================== */

/* --------------------------------------------------------------------------
   01. ROOT VARIABLES & COLOR PALETTE
   -------------------------------------------------------------------------- */
:root {
    --bg-dark: #07090e;
    --bg-secondary: #0d111a;
    --bg-card: rgba(15, 22, 36, 0.65);
    --bg-card-hover: rgba(22, 32, 52, 0.8);
    
    --cyan-neon: #00f2fe;
    --cyan-glow: rgba(0, 242, 254, 0.35);
    --purple-neon: #a855f7;
    --purple-glow: rgba(168, 85, 247, 0.35);
    --blue-neon: #3b82f6;
    --blue-glow: rgba(59, 130, 246, 0.35);
    --gold-neon: #fbbf24;

    --text-main: #f3f4f6;
    --text-muted: #9ca3af;
    --text-dim: #6b7280;

    --glass-bg: rgba(15, 23, 42, 0.65);
    --glass-border: rgba(255, 255, 255, 0.1);
    --glass-border-hover: rgba(0, 242, 254, 0.4);
    --glass-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.4);

    --gradient-primary: linear-gradient(135deg, #00f2fe 0%, #3b82f6 50%, #a855f7 100%);
    --gradient-cyan-purple: linear-gradient(135deg, #00f2fe 0%, #a855f7 100%);
    --gradient-card-border: linear-gradient(135deg, rgba(0, 242, 254, 0.5), rgba(168, 85, 247, 0.5));

    --font-heading: 'Outfit', sans-serif;
    --font-body: 'Inter', sans-serif;
    --font-mono: 'Fira Code', monospace;

    --radius-sm: 8px;
    --radius-md: 14px;
    --radius-lg: 24px;
    --radius-full: 9999px;

    --transition-fast: 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    --transition-normal: 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    --transition-slow: 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

/* --------------------------------------------------------------------------
   02. RESET & GLOBAL STYLES (MOBILE FIRST)
   -------------------------------------------------------------------------- */
*, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

html, body {
    max-width: 100%;
    overflow-x: hidden; /* Prevent horizontal scroll globally */
}

html {
    scroll-behavior: smooth;
    font-size: 14px; /* Base 14px on mobile for better fit */
}

body {
    background-color: var(--bg-dark);
    color: var(--text-main);
    font-family: var(--font-body);
    line-height: 1.6;
    position: relative;
    min-height: 100vh;
}

::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: var(--bg-dark); }
::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.15); border-radius: var(--radius-full); }
::-webkit-scrollbar-thumb:hover { background: var(--cyan-neon); }

a { color: inherit; text-decoration: none; transition: var(--transition-fast); }
ul { list-style: none; }
img, video, svg, iframe, canvas { max-width: 100%; height: auto; display: block; object-fit: cover; }

/* --------------------------------------------------------------------------
   03. BACKGROUND CANVAS & AMBIENT ORBS
   -------------------------------------------------------------------------- */
#bg-canvas {
    position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -2; pointer-events: none;
}

.ambient-orb {
    position: fixed; border-radius: 50%; filter: blur(80px); z-index: -1; pointer-events: none;
    opacity: 0.25; animation: orbPulse 12s infinite alternate ease-in-out;
}
.orb-1 { top: -50px; left: -50px; width: 200px; height: 200px; background: var(--cyan-neon); }
.orb-2 { bottom: 5%; right: -50px; width: 250px; height: 250px; background: var(--purple-neon); animation-delay: 4s; }
.orb-3 { top: 40%; left: 20%; width: 180px; height: 180px; background: var(--blue-neon); animation-delay: 8s; }

@keyframes orbPulse {
    0% { transform: scale(1) translate(0, 0); opacity: 0.2; }
    50% { transform: scale(1.1) translate(15px, -15px); opacity: 0.35; }
    100% { transform: scale(0.9) translate(-10px, 10px); opacity: 0.2; }
}

.mouse-glow { display: none; } /* Disabled on mobile natively */

/* --------------------------------------------------------------------------
   04. REUSABLE UTILITIES & COMPONENTS (MOBILE DEFAULT)
   -------------------------------------------------------------------------- */
.container {
    width: 100%;
    max-width: 100%;
    margin: 0 auto;
    padding: 0 1rem; /* Edge padding */
}

.section {
    padding: 3.5rem 0; /* Reduced vertical padding for mobile */
    position: relative;
}

.section-header {
    text-align: center;
    max-width: 100%;
    margin: 0 auto 2.5rem;
}

.section-tag {
    display: inline-flex; align-items: center; gap: 0.5rem;
    padding: 0.35rem 0.85rem; background: rgba(0, 242, 254, 0.1); border: 1px solid rgba(0, 242, 254, 0.25);
    border-radius: var(--radius-full); color: var(--cyan-neon); font-size: 0.75rem;
    font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 0.75rem;
}

.section-title {
    font-family: var(--font-heading);
    font-size: clamp(1.6rem, 6vw, 2.8rem);
    font-weight: 800; line-height: 1.2; margin-bottom: 0.5rem;
}

.section-subtitle {
    color: var(--text-muted); font-size: clamp(0.9rem, 3vw, 1.1rem);
}

.gradient-text { background: var(--gradient-primary); -webkit-background-clip: text; -webkit-text-fill-color: transparent; display: inline-block; }

.glass-card {
    background: var(--glass-bg); backdrop-filter: blur(16px) saturate(180%); -webkit-backdrop-filter: blur(16px) saturate(180%);
    border: 1px solid var(--glass-border); border-radius: var(--radius-md); box-shadow: var(--glass-shadow);
    transition: var(--transition-normal); position: relative; overflow: hidden; padding: 1.25rem;
}

/* Button System */
.btn {
    display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem;
    padding: 0.7rem 1.4rem; font-family: var(--font-body); font-size: 0.9rem; font-weight: 600;
    border-radius: var(--radius-full); cursor: pointer; transition: var(--transition-normal); border: 1px solid transparent;
}
.btn-primary { background: var(--gradient-primary); color: #ffffff; box-shadow: 0 4px 15px rgba(0, 242, 254, 0.3); }
.btn-secondary { background: rgba(168, 85, 247, 0.2); border-color: var(--purple-neon); color: #ffffff; }
.btn-outline { background: rgba(255, 255, 255, 0.05); border-color: rgba(255, 255, 255, 0.2); color: var(--text-main); }
.btn-sm { padding: 0.5rem 1rem; font-size: 0.8rem; }
.btn-full { width: 100%; }

/* Badges */
.badge { display: inline-flex; align-items: center; padding: 0.2rem 0.6rem; font-size: 0.7rem; font-weight: 600; border-radius: var(--radius-full); }
.badge-cyan { background: rgba(0, 242, 254, 0.15); color: var(--cyan-neon); border: 1px solid rgba(0, 242, 254, 0.3); }
.badge-purple { background: rgba(168, 85, 247, 0.15); color: var(--purple-neon); border: 1px solid rgba(168, 85, 247, 0.3); }

/* Custom Colors */
.cyan-glow { color: var(--cyan-neon); text-shadow: 0 0 15px var(--cyan-glow); }
.purple-glow { color: var(--purple-neon); text-shadow: 0 0 15px var(--purple-glow); }
.blue-glow { color: var(--blue-neon); text-shadow: 0 0 15px var(--blue-glow); }
.green-glow { color: #4ade80; text-shadow: 0 0 15px rgba(74,222,128,0.4); }
.gold-glow { color: var(--gold-neon); text-shadow: 0 0 15px rgba(251, 191, 36, 0.4); }

/* --------------------------------------------------------------------------
   05. NAVIGATION (MOBILE DEFAULT)
   -------------------------------------------------------------------------- */
.navbar {
    position: fixed; top: 0; left: 0; width: 100%; z-index: 100;
    padding: 1rem 0; transition: var(--transition-normal);
}
.navbar.scrolled {
    padding: 0.75rem 0; background: rgba(7, 9, 14, 0.95); backdrop-filter: blur(20px);
    border-bottom: 1px solid rgba(255, 255, 255, 0.1); box-shadow: 0 5px 20px rgba(0, 0, 0, 0.5);
}
.nav-container { display: flex; align-items: center; justify-content: space-between; max-width: 100%; padding: 0 1rem; margin: 0 auto; }

.nav-logo { font-family: var(--font-mono); font-size: 1.1rem; font-weight: 700; display: flex; align-items: center; z-index: 102; }
.logo-bracket { color: var(--cyan-neon); } .logo-text { color: var(--text-main); } .logo-slash { color: var(--purple-neon); }

.hamburger {
    display: flex; background: none; border: none; cursor: pointer; flex-direction: column; gap: 5px; padding: 0.5rem; z-index: 102;
}
.hamburger .bar { width: 24px; height: 2px; background: var(--text-main); transition: var(--transition-normal); border-radius: 2px; }
.hamburger.active .bar:nth-child(1) { transform: translateY(7px) rotate(45deg); }
.hamburger.active .bar:nth-child(2) { opacity: 0; }
.hamburger.active .bar:nth-child(3) { transform: translateY(-7px) rotate(-45deg); }

/* Mobile Drawer Nav */
.nav-menu {
    position: fixed; top: 0; right: -100%; width: 85%; max-width: 320px; height: 100vh;
    background: rgba(7, 9, 14, 0.98); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
    padding: 5rem 1.5rem 2rem; transition: right 0.35s cubic-bezier(0.4, 0, 0.2, 1);
    border-left: 1px solid rgba(255, 255, 255, 0.1); z-index: 101; display: flex; flex-direction: column;
}
.nav-menu.active { right: 0; }
.nav-list { display: flex; flex-direction: column; gap: 1.5rem; width: 100%; }
.nav-link { font-size: 1.1rem; font-weight: 500; color: var(--text-muted); display: block; padding: 0.5rem 0; border-bottom: 1px solid rgba(255,255,255,0.05); }
.nav-actions { margin-top: 2rem; display: flex; flex-direction: column; gap: 1rem; }
.nav-cta { display: flex; width: 100%; justify-content: center; }

/* --------------------------------------------------------------------------
   06. HERO SECTION (MOBILE DEFAULT)
   -------------------------------------------------------------------------- */
.hero-section {
    min-height: auto; padding-top: 6.5rem; padding-bottom: 3rem; display: flex; flex-direction: column; align-items: center; position: relative;
}
.hero-container {
    display: flex; flex-direction: column; gap: 2.5rem; align-items: center; text-align: center; width: 100%;
}
/* Reorder on mobile: Image on top, text below */
.hero-content { order: 2; display: flex; flex-direction: column; align-items: center; width: 100%; }
.hero-visual { order: 1; display: flex; justify-content: center; width: 100%; }

.profile-wrapper { position: relative; width: clamp(160px, 45vw, 240px); aspect-ratio: 1; margin: 0 auto; }
.profile-img-container { position: absolute; inset: 0; border-radius: 50%; overflow: hidden; border: 3px solid rgba(255, 255, 255, 0.2); background: var(--bg-secondary); }
.profile-img { width: 100%; height: 100%; object-fit: cover; }
.profile-glow-ring, .profile-pulse-ring { display: none; } /* Hide heavy rings on mobile by default */
.floating-tech-badge { display: none; } /* Hide floating badges on mobile */

.hero-greeting { display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.35rem 0.85rem; background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: var(--radius-full); font-size: 0.8rem; color: var(--cyan-neon); margin-bottom: 0.75rem; }
.open-to-work-badge { display: flex; flex-direction: column; align-items: center; gap: 0.3rem; padding: 0.4rem 0.8rem; background: rgba(34, 197, 94, 0.1); border: 1px solid rgba(34, 197, 94, 0.4); border-radius: var(--radius-md); font-size: 0.7rem; font-weight: 600; color: #4ade80; margin-bottom: 1.2rem; text-align: center; }
.otw-pulse { display: none; }
.hero-title { font-family: var(--font-heading); font-size: clamp(2rem, 8vw, 3.5rem); font-weight: 800; line-height: 1.15; margin-bottom: 0.5rem; }
.hero-name { display: block; }
.hero-subtitle-wrapper { font-family: var(--font-mono); font-size: clamp(0.85rem, 3.5vw, 1.2rem); font-weight: 600; margin-bottom: 1.25rem; display: flex; flex-wrap: wrap; justify-content: center; gap: 0.4rem; }
.hero-typing { border-right: 2px solid var(--cyan-neon); white-space: normal; } /* Normal wrap on mobile */
.hero-description { color: var(--text-muted); font-size: clamp(0.9rem, 4vw, 1rem); line-height: 1.6; margin-bottom: 1.5rem; width: 100%; }

.hero-ctas { display: flex; flex-direction: column; width: 100%; gap: 0.75rem; margin-bottom: 1.5rem; }
.hero-ctas .btn { width: 100%; }
.hero-contact-strip { display: flex; flex-direction: column; width: 100%; gap: 0.5rem; align-items: center; }
.hero-badge { width: 100%; justify-content: center; }

/* --------------------------------------------------------------------------
   07. ABOUT (MOBILE DEFAULT)
   -------------------------------------------------------------------------- */
.about-grid-enhanced { display: flex; flex-direction: column; gap: 1.5rem; width: 100%; }
.about-left-col, .about-right-col { display: flex; flex-direction: column; gap: 1.25rem; width: 100%; }
.about-photo-card { padding: 1rem; width: 100%; }
.photo-container { position: relative; border-radius: var(--radius-md); overflow: hidden; border: 2px solid rgba(0, 242, 254, 0.2); }
.srijan-portrait { width: 100%; aspect-ratio: 1; object-fit: cover; }
.photo-overlay-badge { bottom: 0.5rem; left: 0.5rem; font-size: 0.7rem; padding: 0.3rem 0.6rem; }
.objective-card, .about-bio-card, .about-edu-card, .about-interests-card { padding: 1.25rem; width: 100%; }

.objective-card h3, .about-bio-card h3, .about-edu-card h3 { font-size: 1.15rem; margin-bottom: 0.75rem; }
.objective-text, .about-bio-card p { font-size: 0.9rem; }
.edu-timeline-list { gap: 1rem; }
.edu-item-header { flex-direction: column; align-items: flex-start; gap: 0.25rem; }
.edu-degree { font-size: 0.95rem; }
.edu-school, .edu-year { font-size: 0.8rem; }
.about-interests-card { display: flex; flex-direction: column; gap: 1rem; }
.interest-item { flex-direction: row; justify-content: flex-start; }

/* --------------------------------------------------------------------------
   08. STATS BAR (MOBILE DEFAULT)
   -------------------------------------------------------------------------- */
.stats-bar { display: flex; flex-direction: column; gap: 1.5rem; padding: 1.5rem; margin-top: 2rem; border-radius: var(--radius-md); }
.stat-item { flex-direction: column; }
.stat-number { font-size: 1.6rem; }
.stat-label { font-size: 0.8rem; }
.stat-divider { width: 50px; height: 1px; background: rgba(255,255,255,0.1); }

/* --------------------------------------------------------------------------
   09. SKILLS (MOBILE DEFAULT)
   -------------------------------------------------------------------------- */
.filter-tabs { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.4rem; margin-bottom: 1.5rem; }
.filter-btn { padding: 0.4rem 0.8rem; font-size: 0.75rem; width: calc(50% - 0.2rem); text-align: center; }
.skills-grid { display: grid; grid-template-columns: 1fr; gap: 1rem; width: 100%; }
.skill-card { padding: 1rem; width: 100%; }
.skill-header { margin-bottom: 0.5rem; }
.skill-icon { font-size: 1.3rem; }
.skill-name { font-size: 0.95rem; }
.skill-desc { font-size: 0.8rem; margin-bottom: 0.75rem; }

/* --------------------------------------------------------------------------
   10. PROJECTS (MOBILE DEFAULT)
   -------------------------------------------------------------------------- */
.projects-grid { display: grid; grid-template-columns: 1fr; gap: 1.5rem; width: 100%; }
.project-card { display: flex; flex-direction: column; width: 100%; }
.project-banner { height: 160px; width: 100%; }
.project-content { padding: 1.25rem; }
.project-header-flex { flex-direction: column; align-items: flex-start; gap: 0.5rem; }
.project-title { font-size: 1.1rem; }
.project-desc { font-size: 0.85rem; }
.project-actions { flex-direction: column; gap: 1rem; align-items: flex-start; }
.project-links { width: 100%; justify-content: space-between; }
.btn-icon-link { width: 34px; height: 34px; font-size: 0.85rem; }

/* --------------------------------------------------------------------------
   11. EXPERIENCE TIMELINE (MOBILE DEFAULT)
   -------------------------------------------------------------------------- */
.experience-timeline { display: flex; flex-direction: column; gap: 1.5rem; }
.timeline-item { padding: 1.25rem; width: 100%; }
.timeline-header { flex-direction: column; align-items: flex-start; gap: 0.5rem; margin-bottom: 0.75rem; }
.timeline-role { font-size: 1.1rem; }
.timeline-meta { flex-direction: column; gap: 0.25rem; font-size: 0.8rem; }
.timeline-desc, .timeline-list { font-size: 0.85rem; }

/* --------------------------------------------------------------------------
   12. CERTIFICATIONS (MOBILE DEFAULT)
   -------------------------------------------------------------------------- */
.cert-grid { display: grid; grid-template-columns: 1fr; gap: 1rem; width: 100%; }
.cert-card { padding: 1rem; flex-direction: column; text-align: left; align-items: flex-start; gap: 1rem; }
.cert-icon-wrap { width: 45px; height: 45px; font-size: 1.2rem; }
.cert-info { width: 100%; }
.cert-name { font-size: 0.95rem; }
.cert-desc { font-size: 0.8rem; }
.cert-meta { flex-direction: column; gap: 0.25rem; }

/* --------------------------------------------------------------------------
   13. RESUME (MOBILE DEFAULT)
   -------------------------------------------------------------------------- */
.resume-card { padding: 1.25rem; width: 100%; }
.resume-header { flex-direction: column; gap: 1rem; align-items: flex-start; text-align: left; }
.resume-avatar { width: 60px; height: 60px; }
.resume-candidate h3 { font-size: 1.2rem; }
.resume-actions { width: 100%; display: flex; flex-direction: column; gap: 0.5rem; }
.resume-actions .btn { width: 100%; }
.resume-body-grid { display: flex; flex-direction: column; gap: 1.5rem; }

/* --------------------------------------------------------------------------
   14. CONTACT (MOBILE DEFAULT)
   -------------------------------------------------------------------------- */
.contact-grid { display: flex; flex-direction: column; gap: 2rem; width: 100%; }
.contact-methods-list { display: flex; flex-direction: column; gap: 1rem; }
.contact-method-card { padding: 1rem; width: 100%; }
.contact-form-wrap { padding: 1.25rem; width: 100%; }
.input-wrap input, .input-wrap textarea { font-size: 0.9rem; padding: 0.8rem; }

/* --------------------------------------------------------------------------
   15. FOOTER (MOBILE DEFAULT)
   -------------------------------------------------------------------------- */
.footer { padding: 3rem 0 1.5rem; }
.footer-grid { display: flex; flex-direction: column; gap: 2rem; text-align: center; }
.footer-col { align-items: center; }
.footer-socials { justify-content: center; }
.footer-bottom { flex-direction: column; gap: 1rem; text-align: center; }

/* --------------------------------------------------------------------------
   16. PRELOADER & MODAL & TOAST & BACK-TO-TOP
   -------------------------------------------------------------------------- */
.preloader { position: fixed; inset: 0; background: var(--bg-dark); z-index: 99999; display: flex; align-items: center; justify-content: center; transition: opacity 0.5s ease, visibility 0.5s ease; }
.preloader.hidden { opacity: 0; visibility: hidden; pointer-events: none; }
.preloader-content { text-align: center; padding: 1rem; }
.preloader-logo-wrap { font-size: clamp(1.2rem, 6vw, 2rem); }
.preloader-bar { width: 150px; margin: 1rem auto 0; }

.page-transition { position: fixed; inset: 0; background: var(--gradient-primary); z-index: 99998; opacity: 0; transform: scaleY(0); transform-origin: top; pointer-events: none; transition: transform 0.4s ease, opacity 0.3s ease; }
.page-transition.active { opacity: 0.1; transform: scaleY(1); }

.modal { position: fixed; inset: 0; background: rgba(0,0,0,0.8); backdrop-filter: blur(5px); z-index: 9999; display: flex; align-items: center; justify-content: center; opacity: 0; visibility: hidden; }
.modal.active { opacity: 1; visibility: visible; }
.modal-card { width: 90%; max-height: 85vh; overflow-y: auto; background: var(--bg-secondary); padding: 1.25rem; border-radius: var(--radius-md); }
.modal-close { position: absolute; top: 1rem; right: 1rem; }

.toast { position: fixed; bottom: 2rem; left: 50%; transform: translateX(-50%) translateY(100px); background: #4ade80; color: #000; padding: 0.8rem 1.5rem; border-radius: var(--radius-full); z-index: 9999; opacity: 0; transition: all 0.3s ease; font-weight: 600; font-size: 0.9rem; text-align: center; width: 90%; max-width: 320px; }
.toast.show { transform: translateX(-50%) translateY(0); opacity: 1; }

.back-to-top { position: fixed; bottom: 1rem; right: 1rem; width: 40px; height: 40px; background: rgba(15,23,42,0.8); border: 1px solid var(--cyan-neon); color: var(--cyan-neon); border-radius: 50%; display: flex; justify-content: center; align-items: center; z-index: 99; opacity: 0; visibility: hidden; transition: 0.3s; }
.back-to-top.active { opacity: 1; visibility: visible; }

/* Disable custom cursor entirely on mobile defaults */
.cursor-dot, .cursor-outline, .cursor-trail { display: none !important; }
* { cursor: auto !important; }

/* ==========================================================================
   PROGRESSIVE ENHANCEMENT (MEDIA QUERIES)
   ========================================================================== */

/* ---- 480px: Phablet Small ---- */
@media (min-width: 480px) {
    .filter-tabs { display: flex; flex-direction: row; }
    .filter-btn { width: auto; }
}

/* ---- 576px: Phablet ---- */
@media (min-width: 576px) {
    html { font-size: 15px; }
    .container { padding: 0 1.25rem; max-width: 540px; }
    .section { padding: 4.5rem 0; }
    
    .hero-greeting { padding: 0.4rem 1rem; font-size: 0.9rem; }
    .open-to-work-badge { flex-direction: row; font-size: 0.8rem; padding: 0.4rem 1.1rem; }
    .otw-pulse { display: block; position: absolute; left: 12px; }
    .hero-ctas { flex-direction: row; justify-content: center; }
    .hero-ctas .btn { width: auto; }
    .hero-contact-strip { flex-direction: row; justify-content: center; }
    
    .about-photo-card { padding: 1.25rem; }
    .srijan-portrait { aspect-ratio: 4/5; }
    
    .stats-bar { flex-direction: row; justify-content: space-around; padding: 2rem; }
    .stat-divider { width: 1px; height: 50px; }
    
    .cert-card { flex-direction: row; align-items: center; }
    .cert-icon-wrap { width: 55px; height: 55px; font-size: 1.4rem; }
    .cert-meta { flex-direction: row; }
}

/* ---- 768px: Tablet ---- */
@media (min-width: 768px) {
    html { font-size: 16px; }
    .container { max-width: 720px; padding: 0 1.5rem; }
    .section { padding: 5rem 0; }
    
    /* Reveal desktop styles for Canvas/Cursor */
    .ambient-orb { filter: blur(120px); opacity: 0.45; }
    .orb-1 { width: 450px; height: 450px; }
    .orb-2 { width: 500px; height: 500px; }
    .orb-3 { width: 400px; height: 400px; }
    
    /* Cursor Reveal */
    @media (pointer: fine) {
        * { cursor: none !important; }
        .cursor-dot, .cursor-outline, .cursor-trail { display: block !important; position: fixed; top: 0; left: 0; transform: translate(-50%, -50%); border-radius: 50%; z-index: 9999; pointer-events: none; opacity: 0; }
        .cursor-dot { width: 10px; height: 10px; background: var(--cyan-neon); box-shadow: 0 0 15px var(--cyan-neon); z-index: 10000; }
        .cursor-outline { width: 45px; height: 45px; border: 1.5px solid rgba(0, 242, 254, 0.6); transition: width 0.3s, height 0.3s; }
        .cursor-trail { width: 6px; height: 6px; background: var(--purple-neon); box-shadow: 0 0 10px var(--purple-neon); }
    }

    .mouse-glow { display: block; }
    
    /* Layouts become 2 column */
    .skills-grid { grid-template-columns: repeat(2, 1fr); gap: 1.5rem; }
    .projects-grid { grid-template-columns: repeat(2, 1fr); gap: 2rem; }
    .cert-grid { grid-template-columns: repeat(2, 1fr); gap: 1.5rem; }
    .contact-grid { flex-direction: row; }
    .contact-methods { flex: 1; }
    .contact-form-wrap { flex: 1.5; }
    
    .footer-grid { flex-direction: row; flex-wrap: wrap; text-align: left; }
    .footer-col { align-items: flex-start; flex: 1; min-width: 200px; }
    .footer-socials { justify-content: flex-start; }
    .footer-bottom { flex-direction: row; justify-content: space-between; }
    
    .resume-header { flex-direction: row; align-items: center; }
    .resume-actions { width: auto; flex-direction: row; margin-left: auto; }
}

/* ---- 992px: Desktop Small ---- */
@media (min-width: 992px) {
    .container { max-width: 960px; }
    
    /* Nav switches to horizontal */
    .hamburger { display: none; }
    .nav-menu { position: static; width: auto; height: auto; background: transparent; backdrop-filter: none; padding: 0; border: none; flex-direction: row; align-items: center; gap: 2rem; }
    .nav-list { flex-direction: row; width: auto; gap: 1.75rem; }
    .nav-link { border: none; padding: 0.3rem 0; font-size: 0.95rem; }
    .nav-actions { margin-top: 0; flex-direction: row; }
    
    .about-grid-enhanced { flex-direction: row; }
    .about-left-col { flex: 0.85; }
    .about-right-col { flex: 1.15; }
    
    .hero-container { flex-direction: row; text-align: left; }
    .hero-content { order: 1; align-items: flex-start; flex: 1.2; }
    .hero-visual { order: 2; flex: 0.8; }
    .hero-subtitle-wrapper { justify-content: flex-start; }
    .hero-ctas { justify-content: flex-start; }
    .hero-contact-strip { justify-content: flex-start; }
    .hero-description { text-align: left; }
    
    .profile-wrapper { width: 320px; }
    .profile-glow-ring, .profile-pulse-ring, .floating-tech-badge { display: flex; }
    
    .skills-grid { grid-template-columns: repeat(3, 1fr); }
    .resume-body-grid { flex-direction: row; }
}

/* ---- 1200px: Desktop Regular ---- */
@media (min-width: 1200px) {
    .container { max-width: 1140px; padding: 0 2rem; }
    .section { padding: 6rem 0; }
    .hero-section { padding-top: 8rem; padding-bottom: 4rem; }
    
    .preloader-logo-wrap { font-size: clamp(2rem, 5vw, 3rem); }
    .preloader-bar { width: 220px; }
}

/* ---- 1440px+: Desktop Large ---- */
@media (min-width: 1440px) {
    .container { max-width: 1240px; }
}

/* ---- Prefers Reduced Motion ---- */
@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
    html { scroll-behavior: auto; }
}
"""
    with open('styles.css', 'w', encoding='utf-8') as f:
        f.write(new_css)

build_css()
