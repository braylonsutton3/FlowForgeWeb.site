from flask import Flask, render_template_string, request

app = Flask(__name__)

SERVICES = [
    {
        "icon": "✦",
        "title": "AI Setup & Automation",
        "price": "Starting at $99",
        "description": (
            "Get practical AI systems built around the way you actually work. "
            "I can create ChatGPT workflows, reusable prompts, customer-response "
            "systems, email workflows, and simple AI automations."
        ),
    },
    {
        "icon": "AI",
        "title": "AI Tutoring",
        "price": "$25–$40/hr",
        "description": (
            "One-on-one help learning how to use AI effectively for school, work, "
            "business, research, organization, and everyday productivity."
        ),
    },
    {
        "icon": "</>",
        "title": "Python / Coding Tutoring",
        "price": "$25–$40/hr",
        "description": (
            "Personal coding help covering beginner Python, debugging, automation, "
            "APIs, HTML/CSS, and the fundamentals of building web projects."
        ),
    },
    {
        "icon": "WEB",
        "title": "Website Build",
        "price": "Starting at $299",
        "description": (
            "A clean, modern, mobile-friendly website built for your business, "
            "service, freelance work, or personal brand with a professional online presence."
        ),
    },
    {
        "icon": "↻",
        "title": "Website Redesign / Fix-Up",
        "price": "Starting at $149",
        "description": (
            "Upgrade an outdated or weak website with improved design, mobile layout, "
            "calls-to-action, contact sections, and a more professional appearance."
        ),
    },
    {
        "icon": "◎",
        "title": "Lead Generation System Setup",
        "price": "Starting at $149",
        "description": (
            "Build a repeatable system for finding, qualifying, organizing, and tracking "
            "potential customers so your outreach is faster and more focused."
        ),
    },
    {
        "icon": "⚙",
        "title": "Business Automation",
        "price": "Starting at $99",
        "description": (
            "Reduce repetitive work by automating spreadsheets, file organization, "
            "reports, lead tracking, and other simple day-to-day business workflows."
        ),
    },
    {
        "icon": "↗",
        "title": "Sales & Outreach Setup",
        "price": "Starting at $99",
        "description": (
            "Get help creating stronger cold emails, call scripts, service offers, "
            "follow-up messages, and a more organized outreach process."
        ),
    },
]

PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description"
          content="Flow Forge Web provides AI setup, coding tutoring, websites, automation, lead generation systems, and business growth tools.">

    <title>Flow Forge Web | AI, Web & Business Solutions</title>

    <style>
        :root {
            --blue: #0b4ea2;
            --blue-dark: #072f68;
            --blue-light: #eaf3ff;
            --yellow: #ffd84d;
            --yellow-soft: #fff7cf;
            --white: #ffffff;
            --off-white: #f7f9fc;
            --text: #172033;
            --muted: #62708a;
            --border: #dce4ef;
            --shadow: 0 14px 40px rgba(15, 57, 106, 0.10);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family:
                Inter, ui-sans-serif, system-ui, -apple-system,
                BlinkMacSystemFont, "Segoe UI", sans-serif;
            background: var(--white);
            color: var(--text);
            line-height: 1.6;
        }

        a {
            color: inherit;
            text-decoration: none;
        }

        .container {
            width: min(1160px, calc(100% - 36px));
            margin: 0 auto;
        }

        /* NAV */
        nav {
            position: sticky;
            top: 0;
            z-index: 100;
            background: rgba(255,255,255,.94);
            backdrop-filter: blur(14px);
            border-bottom: 1px solid rgba(220,228,239,.85);
        }

        .nav-inner {
            min-height: 74px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 20px;
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 11px;
            font-size: 1.15rem;
            font-weight: 900;
            color: var(--blue-dark);
            letter-spacing: -.02em;
        }

        .brand-mark {
            width: 38px;
            height: 38px;
            display: grid;
            place-items: center;
            border-radius: 11px;
            background: var(--yellow);
            color: var(--blue-dark);
            font-weight: 1000;
            box-shadow: 0 7px 20px rgba(255,216,77,.35);
        }

        .nav-links {
            display: flex;
            align-items: center;
            gap: 26px;
            font-size: .94rem;
            font-weight: 700;
            color: #40506a;
        }

        .nav-links a:hover {
            color: var(--blue);
        }

        .nav-btn {
            padding: 10px 18px;
            border-radius: 999px;
            background: var(--blue);
            color: white !important;
        }

        .nav-btn:hover {
            background: var(--blue-dark);
        }

        /* HERO */
        .hero {
            position: relative;
            overflow: hidden;
            padding: 100px 0 90px;
            background:
                radial-gradient(circle at 90% 10%, rgba(255,216,77,.35), transparent 29%),
                linear-gradient(135deg, #f9fbff 0%, #ffffff 47%, #f1f7ff 100%);
        }

        .hero:before {
            content: "";
            position: absolute;
            width: 420px;
            height: 420px;
            border: 60px solid rgba(11,78,162,.04);
            border-radius: 50%;
            right: -170px;
            bottom: -160px;
        }

        .hero-grid {
            display: grid;
            grid-template-columns: 1.18fr .82fr;
            align-items: center;
            gap: 70px;
        }

        .eyebrow {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: var(--yellow-soft);
            color: #6a5400;
            padding: 8px 13px;
            border-radius: 999px;
            font-size: .82rem;
            font-weight: 800;
            margin-bottom: 22px;
            border: 1px solid #f4df7d;
        }

        h1 {
            font-size: clamp(2.75rem, 6vw, 5.3rem);
            line-height: .98;
            letter-spacing: -.055em;
            color: var(--blue-dark);
            max-width: 790px;
        }

        .hero-highlight {
            color: var(--blue);
            position: relative;
            white-space: nowrap;
        }

        .hero-highlight:after {
            content: "";
            position: absolute;
            height: 11px;
            left: 0;
            right: 0;
            bottom: 1px;
            background: var(--yellow);
            z-index: -1;
            transform: rotate(-1deg);
        }

        .hero-text {
            max-width: 670px;
            color: var(--muted);
            font-size: 1.1rem;
            margin-top: 27px;
        }

        .hero-actions {
            display: flex;
            flex-wrap: wrap;
            gap: 13px;
            margin-top: 34px;
        }

        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-height: 50px;
            padding: 0 23px;
            border-radius: 12px;
            font-weight: 800;
            border: 2px solid transparent;
            transition: .2s ease;
        }

        .btn-primary {
            background: var(--blue);
            color: white;
            box-shadow: 0 10px 25px rgba(11,78,162,.2);
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            background: var(--blue-dark);
        }

        .btn-secondary {
            background: white;
            color: var(--blue);
            border-color: var(--border);
        }

        .btn-secondary:hover {
            border-color: var(--blue);
            transform: translateY(-2px);
        }

        .hero-card {
            background: var(--blue-dark);
            color: white;
            border-radius: 28px;
            padding: 35px;
            box-shadow: 0 30px 70px rgba(7,47,104,.22);
            position: relative;
            overflow: hidden;
        }

        .hero-card:after {
            content: "";
            position: absolute;
            width: 180px;
            height: 180px;
            border-radius: 50%;
            background: var(--yellow);
            right: -85px;
            top: -85px;
        }

        .hero-card-label {
            color: var(--yellow);
            font-weight: 850;
            font-size: .86rem;
            letter-spacing: .06em;
            text-transform: uppercase;
            margin-bottom: 12px;
        }

        .hero-card h3 {
            font-size: 1.75rem;
            line-height: 1.15;
            margin-bottom: 22px;
            max-width: 340px;
        }

        .mini-list {
            display: grid;
            gap: 12px;
        }

        .mini-item {
            display: flex;
            gap: 12px;
            align-items: flex-start;
            color: #dce8f7;
            font-size: .94rem;
        }

        .check {
            width: 22px;
            height: 22px;
            flex: 0 0 22px;
            display: grid;
            place-items: center;
            background: var(--yellow);
            color: var(--blue-dark);
            border-radius: 50%;
            font-size: .72rem;
            font-weight: 1000;
        }

        /* GENERAL SECTION */
        section {
            padding: 86px 0;
        }

        .section-label {
            color: var(--blue);
            text-transform: uppercase;
            letter-spacing: .13em;
            font-weight: 900;
            font-size: .78rem;
            margin-bottom: 12px;
        }

        .section-title {
            font-size: clamp(2rem, 4vw, 3.25rem);
            line-height: 1.08;
            letter-spacing: -.04em;
            color: var(--blue-dark);
            max-width: 770px;
        }

        .section-copy {
            margin-top: 18px;
            max-width: 760px;
            color: var(--muted);
            font-size: 1.03rem;
        }

        /* AI SECTION */
        .ai-section {
            background: var(--blue-dark);
            color: white;
        }

        .ai-grid {
            display: grid;
            grid-template-columns: .9fr 1.1fr;
            gap: 72px;
            align-items: center;
        }

        .ai-section .section-title {
            color: white;
        }

        .ai-section .section-copy {
            color: #c6d5e9;
        }

        .ai-stat {
            background: rgba(255,255,255,.07);
            border: 1px solid rgba(255,255,255,.11);
            border-radius: 24px;
            padding: 34px;
        }

        .ai-stat h3 {
            color: var(--yellow);
            font-size: 2rem;
            margin-bottom: 10px;
        }

        .ai-stat p {
            color: #dae5f4;
        }

        .ai-points {
            display: grid;
            grid-template-columns: repeat(2,1fr);
            gap: 15px;
            margin-top: 20px;
        }

        .ai-point {
            padding: 20px;
            border-radius: 16px;
            background: rgba(255,255,255,.065);
            border: 1px solid rgba(255,255,255,.08);
        }

        .ai-point strong {
            display: block;
            color: white;
            margin-bottom: 5px;
        }

        .ai-point span {
            color: #bdcde1;
            font-size: .9rem;
        }

        /* SERVICES */
        #services {
            background: var(--off-white);
        }

        .services-head {
            display: flex;
            align-items: end;
            justify-content: space-between;
            gap: 30px;
            margin-bottom: 42px;
        }

        .services-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
        }

        .service-card {
            position: relative;
            background: white;
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 30px;
            transition: .22s ease;
            overflow: hidden;
        }

        .service-card:hover {
            transform: translateY(-5px);
            box-shadow: var(--shadow);
            border-color: #bfd4ec;
        }

        .service-card:before {
            content: "";
            width: 5px;
            height: 55px;
            border-radius: 0 8px 8px 0;
            background: var(--yellow);
            position: absolute;
            left: 0;
            top: 28px;
        }

        .service-top {
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            gap: 20px;
            margin-bottom: 18px;
        }

        .service-icon {
            width: 50px;
            height: 50px;
            display: grid;
            place-items: center;
            border-radius: 14px;
            background: var(--blue-light);
            color: var(--blue);
            font-weight: 1000;
            font-size: .85rem;
        }

        .price {
            display: inline-block;
            background: var(--yellow-soft);
            border: 1px solid #f4df7d;
            color: #705800;
            border-radius: 999px;
            padding: 7px 12px;
            font-weight: 850;
            font-size: .82rem;
            white-space: nowrap;
        }

        .service-card h3 {
            font-size: 1.28rem;
            color: var(--blue-dark);
            margin-bottom: 10px;
        }

        .service-card p {
            color: var(--muted);
            font-size: .95rem;
        }

        /* HOW IT HELPS */
        .benefits-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            margin-top: 42px;
        }

        .benefit {
            padding: 27px;
            border-radius: 18px;
            border: 1px solid var(--border);
            background: white;
        }

        .benefit-number {
            width: 38px;
            height: 38px;
            display: grid;
            place-items: center;
            border-radius: 50%;
            background: var(--yellow);
            color: var(--blue-dark);
            font-weight: 900;
            margin-bottom: 18px;
        }

        .benefit h3 {
            color: var(--blue-dark);
            margin-bottom: 8px;
        }

        .benefit p {
            color: var(--muted);
            font-size: .94rem;
        }

        /* ABOUT */
        .about {
            background: linear-gradient(135deg, #f2f7ff, #ffffff);
        }

        .about-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 68px;
            align-items: center;
        }

        .about-box {
            border-radius: 24px;
            background: var(--yellow);
            padding: 38px;
            color: var(--blue-dark);
            box-shadow: 0 25px 60px rgba(136,104,0,.12);
        }

        .about-box .big {
            font-weight: 950;
            font-size: clamp(2rem,4vw,3rem);
            line-height: 1.07;
            letter-spacing: -.04em;
            margin-bottom: 16px;
        }

        /* CONTACT */
        .contact-wrap {
            display: grid;
            grid-template-columns: .9fr 1.1fr;
            gap: 55px;
            align-items: start;
        }

        .contact-card {
            background: white;
            border: 1px solid var(--border);
            box-shadow: var(--shadow);
            border-radius: 22px;
            padding: 30px;
        }

        .form-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 14px;
        }

        .field-full {
            grid-column: 1 / -1;
        }

        label {
            display: block;
            font-size: .84rem;
            font-weight: 800;
            color: #374964;
            margin-bottom: 6px;
        }

        input, select, textarea {
            width: 100%;
            border: 1px solid #cad6e4;
            background: #fbfcff;
            border-radius: 11px;
            padding: 13px 14px;
            font: inherit;
            color: var(--text);
            outline: none;
        }

        input:focus, select:focus, textarea:focus {
            border-color: var(--blue);
            box-shadow: 0 0 0 3px rgba(11,78,162,.08);
        }

        textarea {
            min-height: 120px;
            resize: vertical;
        }

        .submit {
            width: 100%;
            border: none;
            cursor: pointer;
            margin-top: 6px;
        }

        .success {
            margin-bottom: 18px;
            padding: 14px 16px;
            border-radius: 12px;
            color: #154d2b;
            background: #e8f8ee;
            border: 1px solid #b6e4c5;
            font-weight: 700;
        }

        .note {
            margin-top: 10px;
            color: #7c8799;
            font-size: .78rem;
        }

        /* FOOTER */
        footer {
            background: var(--blue-dark);
            color: #c6d5e9;
            padding: 34px 0;
        }

        .footer-inner {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 20px;
        }

        footer strong {
            color: white;
        }

        /* RESPONSIVE */
        @media (max-width: 850px) {
            .nav-links a:not(.nav-btn) {
                display: none;
            }

            .hero-grid,
            .ai-grid,
            .about-grid,
            .contact-wrap {
                grid-template-columns: 1fr;
            }

            .hero {
                padding-top: 72px;
            }

            .hero-grid {
                gap: 38px;
            }

            .services-grid {
                grid-template-columns: 1fr;
            }

            .benefits-grid {
                grid-template-columns: 1fr;
            }

            .services-head {
                align-items: flex-start;
                flex-direction: column;
            }
        }

        @media (max-width: 570px) {
            section {
                padding: 65px 0;
            }

            .container {
                width: min(100% - 24px, 1160px);
            }

            .hero {
                padding: 62px 0 65px;
            }

            h1 {
                font-size: 2.7rem;
            }

            .hero-card {
                padding: 27px;
            }

            .ai-points {
                grid-template-columns: 1fr;
            }

            .service-card {
                padding: 24px;
            }

            .service-top {
                flex-direction: column;
            }

            .form-grid {
                grid-template-columns: 1fr;
            }

            .field-full {
                grid-column: auto;
            }

            .footer-inner {
                flex-direction: column;
                align-items: flex-start;
            }
        }
    </style>
</head>

<body>

<nav>
    <div class="container nav-inner">
        <a href="#" class="brand">
            <span class="brand-mark">F</span>
            Flow Forge Web
        </a>

        <div class="nav-links">
            <a href="#services">Services</a>
            <a href="#why-us">Why Us</a>
            <a href="#about">About</a>
            <a href="#contact" class="nav-btn">Get Started</a>
        </div>
    </div>
</nav>


<header class="hero">
    <div class="container hero-grid">

        <div>
            <div class="eyebrow">AI • WEB DEVELOPMENT • AUTOMATION • GROWTH</div>

            <h1>
                Build smarter.
                <span class="hero-highlight">Grow faster.</span>
            </h1>

            <p class="hero-text">
                Flow Forge Web helps individuals and small businesses use AI,
                websites, automation, coding, and smarter outreach to save time,
                improve their online presence, and create new opportunities.
            </p>

            <div class="hero-actions">
                <a href="#services" class="btn btn-primary">View Services</a>
                <a href="#contact" class="btn btn-secondary">Request a Quote</a>
            </div>
        </div>

        <div class="hero-card">
            <div class="hero-card-label">What We Help With</div>
            <h3>Practical digital solutions without unnecessary complexity.</h3>

            <div class="mini-list">
                <div class="mini-item">
                    <span class="check">✓</span>
                    <span>Use AI more effectively in work, school, and business.</span>
                </div>

                <div class="mini-item">
                    <span class="check">✓</span>
                    <span>Create or improve a clean professional website.</span>
                </div>

                <div class="mini-item">
                    <span class="check">✓</span>
                    <span>Automate repetitive business and data tasks.</span>
                </div>

                <div class="mini-item">
                    <span class="check">✓</span>
                    <span>Build better systems for leads, sales, and outreach.</span>
                </div>
            </div>
        </div>

    </div>
</header>


<section class="ai-section">
    <div class="container ai-grid">

        <div>
            <div class="section-label" style="color:#ffd84d;">The opportunity</div>

            <h2 class="section-title">
                AI is growing — and it isn't going anywhere.
            </h2>

            <p class="section-copy">
                AI is becoming part of how people learn, communicate, sell,
                build, research, and run businesses. The advantage is not simply
                having access to AI — it is knowing how to use it effectively.
            </p>

            <p class="section-copy">
                Flow Forge Web helps make these tools practical, understandable,
                and useful for the work you are already doing.
            </p>
        </div>

        <div class="ai-stat">
            <h3>Work smarter with technology.</h3>

            <p>
                You do not need to become a programmer or AI expert to benefit
                from modern tools. The right setup can reduce repetitive work
                and help you move faster.
            </p>

            <div class="ai-points">
                <div class="ai-point">
                    <strong>Save Time</strong>
                    <span>Reduce repetitive work and manual processes.</span>
                </div>

                <div class="ai-point">
                    <strong>Learn Faster</strong>
                    <span>Understand AI and coding through 1-on-1 tutoring.</span>
                </div>

                <div class="ai-point">
                    <strong>Look Professional</strong>
                    <span>Give customers a cleaner digital experience.</span>
                </div>

                <div class="ai-point">
                    <strong>Find Opportunities</strong>
                    <span>Create better systems for outreach and growth.</span>
                </div>
            </div>
        </div>

    </div>
</section>


<section id="services">
    <div class="container">

        <div class="services-head">
            <div>
                <div class="section-label">Services & pricing</div>
                <h2 class="section-title">
                    Choose exactly what you need.
                </h2>

                <p class="section-copy">
                    Straightforward services for individuals, students,
                    entrepreneurs, and small businesses.
                </p>
            </div>
        </div>

        <div class="services-grid">
            {% for service in services %}
            <article class="service-card">

                <div class="service-top">
                    <div class="service-icon">{{ service.icon }}</div>
                    <span class="price">{{ service.price }}</span>
                </div>

                <h3>{{ service.title }}</h3>

                <p>{{ service.description }}</p>

            </article>
            {% endfor %}
        </div>

    </div>
</section>


<section id="why-us">
    <div class="container">

        <div class="section-label">How this can help</div>

        <h2 class="section-title">
            Technology should make your life easier, not more complicated.
        </h2>

        <p class="section-copy">
            Every service is focused on helping you accomplish something useful:
            saving time, learning a skill, improving your business, or getting
            more value from the technology available to you.
        </p>

        <div class="benefits-grid">

            <div class="benefit">
                <div class="benefit-number">1</div>
                <h3>Save Time</h3>
                <p>
                    Automate repetitive work and create systems that make daily
                    tasks easier to manage.
                </p>
            </div>

            <div class="benefit">
                <div class="benefit-number">2</div>
                <h3>Build Valuable Skills</h3>
                <p>
                    Learn AI and coding one-on-one with explanations focused on
                    understanding, not memorization.
                </p>
            </div>

            <div class="benefit">
                <div class="benefit-number">3</div>
                <h3>Grow Your Business</h3>
                <p>
                    Improve your website, outreach, lead systems, and digital
                    workflow so you can focus more energy on customers.
                </p>
            </div>

        </div>
    </div>
</section>


<section class="about" id="about">
    <div class="container about-grid">

        <div>
            <div class="section-label">About Flow Forge Web</div>

            <h2 class="section-title">
                Modern digital help without the agency-sized price tag.
            </h2>

            <p class="section-copy">
                Flow Forge Web focuses on practical technology for real people
                and small businesses. We work across web development, AI,
                automation, coding education, and business-growth systems.
            </p>

            <p class="section-copy">
                The goal is simple: understand what you are trying to accomplish,
                choose the right tools, and build a solution that is useful,
                affordable, and easy to understand.
            </p>
        </div>

        <div class="about-box">
            <div class="big">
                Websites.<br>
                AI.<br>
                Automation.<br>
                Growth.
            </div>

            <p>
                One place for the digital tools and guidance that can help you
                learn faster, work smarter, and build something better.
            </p>
        </div>

    </div>
</section>


<section id="contact">
    <div class="container contact-wrap">

        <div>
            <div class="section-label">Get started</div>

            <h2 class="section-title">
                Tell me what you want to accomplish.
            </h2>

            <p class="section-copy">
                Choose the service you are interested in and briefly explain
                what you need. Pricing may vary depending on the size and
                complexity of the project.
            </p>

            <p class="section-copy">
                Not sure which service fits? Describe the problem and I can help
                determine the simplest solution.
            </p>
        </div>

        <div class="contact-card">

            {% if submitted %}
            <div class="success">
                Thanks! Your request was received on this page.
                Replace this demo submission system with your preferred email
                or form service before taking the site live.
            </div>
            {% endif %}

            <form method="POST" action="#contact">
                <div class="form-grid">

                    <div>
                        <label for="name">Name</label>
                        <input
                            id="name"
                            name="name"
                            type="text"
                            placeholder="Your name"
                            required>
                    </div>

                    <div>
                        <label for="email">Email</label>
                        <input
                            id="email"
                            name="email"
                            type="email"
                            placeholder="you@example.com"
                            required>
                    </div>

                    <div class="field-full">
                        <label for="service">Service</label>

                        <select id="service" name="service">
                            {% for service in services %}
                            <option>{{ service.title }}</option>
                            {% endfor %}
                            <option>Not sure yet</option>
                        </select>
                    </div>

                    <div class="field-full">
                        <label for="message">What do you need help with?</label>

                        <textarea
                            id="message"
                            name="message"
                            placeholder="Tell me a little about what you want to accomplish..."
                            required></textarea>
                    </div>

                    <div class="field-full">
                        <button type="submit" class="btn btn-primary submit">
                            Request a Quote
                        </button>

                        <div class="note">
                            This demo form currently confirms the submission on
                            the website. Add your email/form provider before launch.
                        </div>
                    </div>

                </div>
            </form>
        </div>

    </div>
</section>


<footer>
    <div class="container footer-inner">
        <div>
            <strong>Flow Forge Web</strong><br>
            AI • Web Development • Automation • Business Growth
        </div>

        <div>
            © 2026 Flow Forge Web. All rights reserved.
        </div>
    </div>
</footer>

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():
    submitted = request.method == "POST"
    return render_template_string(
        PAGE,
        services=SERVICES,
        submitted=submitted
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
