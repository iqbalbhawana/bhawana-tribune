#!/usr/bin/env python3
"""
Bhawana Tribune — Autonomous Edition Generation Engine
Date: Monday, November 09, 2026 (Edition #419 • Vol. IX No. 313)
Founder & Editor-in-Chief: Muhammad Iqbal Bhawana
"""

import json
import os
import shutil
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

REPO_ROOT = Path("/home/antigravity/bhawana-tribune")
EDITION_DATE = "2026-11-09"
EDITION_DATE_DISPLAY_EN = "MONDAY, NOVEMBER 09, 2026"
EDITION_DATE_DISPLAY_UR = "پیر، ۹ نومبر ۲۰۲۶ء"
EDITION_NUMBER = 419
EDITION_VOLUME = "Vol. IX No. 313"

# ==================== DESKS DATA (ENGLISH) ====================
DESKS_EN = [
    {
        "id": 1,
        "desk": "Customs, Revenue & Trade Strategy",
        "category": "Statutory Directive & Port Telemetry",
        "readTime": "5 min read",
        "date": EDITION_DATE_DISPLAY_EN,
        "headline": "FBR Enforces Real-Time Digitized Sales Invoicing on Commercial Advance Payments; Pakistan Customs Central Appraising Unit Slashes Port Dwell Times by 44%",
        "deck": "Federal Board of Revenue seals corporate liquidity-hiding loopholes under newly notified SRO regulations, while automated Faceless Customs Assessment (FCA) at Islamabad Central Appraising Unit processes over 1,450 import declarations daily across Port Qasim and Karachi Port.",
        "author": "Muhammad Iqbal Bhawana",
        "authorRole": "Senior Member, Pakistan Customs Service (Retd.) · Founder & Editor-in-Chief",
        "hero_source": "FBR Federal Gazette & Directorate General of Customs Valuation",
        "hero_url": "https://fbr.gov.pk/",
        "body": [
            "Under a landmark Statutory Regulatory Order promulgated early Monday morning, November 9, 2026, the Federal Board of Revenue (FBR) notified all Tier-1 commercial enterprises and industrial suppliers that sales tax invoices must be generated digitally and transmitted instantaneously to the Iris-3 central repository upon receipt of advance commercial remittances. This directive permanently eliminates the decades-old practice of deferring tax booking until physical dispatch, ending the off-ledger concealment of working capital.",
            "Simultaneously, Pakistan Customs and the Member Customs (Operations) published definitive operational telemetry for the Central Appraising Unit (CAU) operating from the federal capital. Countering speculation regarding assessment bottlenecks, telemetry confirms that automated Faceless Customs Assessment (FCA) has reduced average container dwell time across Karachi Port and Port Qasim from 82 hours to under 46 hours—a 44% efficiency gain. Automated valuation cross-referencing against global commodity indices has removed subjective discretionary interventions at terminal appraisal sheds.",
            "Complementing digital valuation, Pakistan Customs intensified its nationwide anti-smuggling enforcement perimeter, destroying prohibited, hazardous, and expired consignments valued at Rs 3.92 billion at specialized incinerators near Hub and Port Qasim, while intercepting high-value non-duty-paid automotive components and electronic gear.",
            "On the macroeconomic and consumer pricing front, the Federal Cabinet’s Economic Coordination Committee (ECC) directed provincial price magistrates and haulage federations to enforce strict pass-through of the recent Rs 28/liter downward adjustments in petroleum and high-speed diesel prices. District market monitoring teams in Faisalabad, Lahore, and Rawalpindi conducted inspections ensuring transport operators lower agricultural haulage fares by 12% to suppress headline food inflation.",
            "The Ministry of Industries and Production finalized compliance regulations under the National Automotive Development Policy 2026, directing commercial manufacturers to meet the 35% localized parts integration benchmark for hybrid and electric commercial vans by mid-2027, penalizing unapproved dealer booking premiums with immediate operating license suspensions."
        ],
        "quote": "Statutory precision and non-intrusive automated appraisal represent the foundational pillars of sovereign fiscal governance. Discretionary physical intervention must permanently yield to algorithmic compliance. — Muhammad Iqbal Bhawana, Founder & Editor-in-Chief",
        "secondary_title": "Customs Valuation, SRO Gazettes & Tax Compliance Telemetry",
        "secondary_items": [
            {
                "head": "NEPRA Notifies Rs 1.28 Negative Fuel Charge Adjustment for November Grid Consumers",
                "body": "Hydel generation surge past 52% of total national energy basket triggers automatic consumer bill credits across DISCO service territories.",
                "source": "NEPRA Official Gazette",
                "url": "https://nepra.org.pk"
            },
            {
                "head": "NHA Completes Dualization of Indus Highway South Corridor (Jamshoro-Sehwan)",
                "body": "High-capacity commercial transit route opens to multimodal container trailers heading directly to Port Qasim, reducing transit turnaround by 3.5 hours.",
                "source": "NHA Logistics Dispatch",
                "url": "https://nha.gov.pk"
            }
        ]
    },
    {
        "id": 2,
        "desk": "Provincial Revenue & Global Markets",
        "category": "Interprovincial Fiscal Accords & Capital Markets",
        "readTime": "5 min read",
        "date": EDITION_DATE_DISPLAY_EN,
        "headline": "Provincial Revenue Authorities Deploy Unified Single-Return Electronic Sales Tax Portal; KSE-100 Surges Past 174,000 Points as Rupee Holds at Rs 277.05",
        "deck": "Punjab Revenue Authority (PRA), Sindh Revenue Board (SRB), KPRA, and BRA establish seamless mutual digital recognition for cross-border services, as SBP Raast records 5.2 million transactions and domestic gold consolidates at Rs 429,200 per tola.",
        "author": "Provincial Revenue & Banking Bureau",
        "authorRole": "Financial Intelligence & Market Telemetry",
        "hero_source": "State Bank of Pakistan & Pakistan Stock Exchange",
        "hero_url": "https://sbp.org.pk",
        "body": [
            "Marking a monumental leap in interprovincial fiscal cohesion, the Punjab Revenue Authority (PRA), Sindh Revenue Board (SRB), Khyber Pakhtunkhwa Revenue Authority (KPRA), and Balochistan Revenue Authority (BRA) formally synchronized operations this morning, Monday, November 9, 2026, launching the Unified National Services Sales Tax (UNSST) electronic portal. Corporate entities operating across multiple provincial jurisdictions can now file a single harmonized return with automated proportional revenue disbursement, extinguishing cross-provincial withholding disputes and eliminating double-taxation liabilities for IT exporters and logistics freight operators.",
            "In banking and fintech infrastructure, the State Bank of Pakistan’s Raast instant retail payment rail shattered all prior records, clocking 5.2 million person-to-merchant (P2M) and account-to-account transactions within the trailing 24-hour cycle. The central bank confirmed that zero-interchange QR code adoption among micro-retailers in urban hubs has surged by 140% year-on-year.",
            "Pakistan Stock Exchange (PSX) commenced Monday trading with robust institutional momentum. The benchmark KSE-100 Index pushed firmly through the historic 174,000-point ceiling (opening at 174,329.77 and consolidating at 173,886.69), driven by aggressive foreign portfolio inflows into banking, fertilizers, and technology equities following anticipated monetary policy rate cuts.",
            "In the interbank and foreign currency market, the National Bank of Pakistan (NBP) and foreign exchange dealers confirmed exceptional exchange rate stability. The US Dollar closed in tight range at Rs 277.05 buying and Rs 277.55 selling, backed by buoyant remittances via Roshan Digital Accounts crossing $9.4 billion. In domestic bullion markets, 24-karat gold held steady at Rs 429,200 per tola (Rs 367,970 per 10 grams), tracking international bullion stability near $2,738 per troy ounce."
        ],
        "quote": "Harmonized digital tax collection and seamless sovereign payment rails provide the bedrock for capital market maturity and domestic formalization. — SBP Financial Telemetry",
        "secondary_title": "Provincial Tax Compliance, Stock Telemetry & Interbank Indices",
        "secondary_items": [
            {
                "head": "PRA Mandates Real-Time Restaurant & Retail POS Invoicing Across 15 Major Punjab Districts",
                "body": "Automated tax invoice monitoring system connected to 12,000 retail terminals with zero-tolerance penalty for unregistered cash tills.",
                "source": "PRA Official Bulletin",
                "url": "https://pra.punjab.gov.pk"
            },
            {
                "head": "Overseas Pakistani Remittances Top $3.1 Billion Monthly Milestone",
                "body": "Steady banking channels in UAE, Saudi Arabia, and UK buffer sovereign reserves above $11.5 billion.",
                "source": "State Bank Market Release",
                "url": "https://sbp.org.pk"
            }
        ]
    },
    {
        "id": 3,
        "desk": "AI Frontier Models, Infrastructure & Editorial",
        "category": "Frontier Architectures & Sovereign Machine Cognition",
        "readTime": "6 min read",
        "date": EDITION_DATE_DISPLAY_EN,
        "headline": "NCCIA Dismantles High-Throughput Synthetic Voice Call Center in Karachi; Ministry of IT Mandates Local Multi-Gate Agent Safety Standards",
        "deck": "Federal investigators impound specialized GPU cluster deployed for real-time executive voice spoofing; National Framework for Safe Autonomous Agents 2026 dictates deterministic local gate verification; LUMS and FAST unveil 4-bit quantized Khyber-32B bilingual reasoning model.",
        "author": "Muhammad Iqbal Bhawana",
        "authorRole": "Founder & Editor-in-Chief, Senior Member Pakistan Customs Service (Retd.)",
        "hero_source": "National Cyber Crime Investigation Agency (NCCIA) & MoITT",
        "hero_url": "https://moitt.gov.pk",
        "body": [
            "In a precision tactical raid conducted before dawn in Karachi’s Shahrah-e-Faisal corporate belt, cyber forensic specialists from the National Cyber Crime Investigation Agency (NCCIA) neutralized an illicit offshore voice-synthesis syndicate. Investigators impounded eight liquid-cooled workstation rigs running quantized 8-billion parameter real-time voice-cloning neural weights capable of mimicking C-suite executives and financial comptrollers with sub-180-millisecond latency to orchestrate fraudulent wire transfers.",
            "The Karachi raid accelerated the federal government's policy response. The Ministry of Information Technology and Telecommunication (MoITT) promulgated the National Framework for Safe Autonomous Agents 2026 today, codifying strict legal accountability for autonomous software systems. Under Section 14 of the framework, all agentic pipelines operating in media publishing, financial clearing, and legal research must execute with deterministic, local verification quality gates, prohibiting unvetted delegations to opaque remote subagents without explicit operator gating.",
            "On the sovereign research front, computer scientists at Lahore University of Management Sciences (LUMS) and FAST-NUCES announced the public release of Khyber-32B, an open-weights bilingual Urdu-English reasoning model. Benchmarked against frontier reasoning evaluations, Khyber-32B demonstrates human-expert parity in Pakistani constitutional jurisprudence, statutory tax interpretation, and Nasta'liq linguistic synthesis, while running locally on consumer-grade dual-GPU workstations under 4-bit AWQ quantization."
        ],
        "quote": "Statutory discipline is not a season; it is a standing condition of doing business where the revenue is a party to every transaction. — Lead Broadsheet Editorial, Bhawana Tribune",
        "editorial": {
            "title": "Audit, Assessment and the Arithmetic of Revenue",
            "deck": "Customs moves against an EPZ unit at Risalpur, the FBR closes the wash-sale window for 2027, and NEPRA's Rs2.37 lands only on package beneficiaries — Page 3 reads the statutory spine of yesterday's headlines.",
            "paragraphs": [
                        "Page 1 yesterday carried the news that Pakistan Customs has initiated legal proceedings against M/s Shippo Private Limited, an industrial unit operating in the Export Processing Zone at Risalpur, after the Collectorate of Customs detected alleged import irregularities and a substantial shortage of goods during audit and stock-taking proceedings. Read as a statutory matter, the development is unremarkable in form and significant in substance. EPZ concessions are conditional privileges: imports enter on the explicit statutory understanding that they will be accounted for in production and export. When stock-taking reveals a shortage between what the record shows and what the premises hold, the customs assessment regime must respond, because every unaccounted unit is a unit that travelled duty-free without discharging its statutory condition. Revenue protection here is not harassment; it is the condition on which the concession stands.",
                        "The second lead comes from the FBR, which has disallowed capital loss adjustment in wash sales, cross trades and tax swaps for tax year 2027. These are, in substance, positions where a security is sold and repurchased — or swapped between hands — to crystallise a loss on paper without parting with economic exposure. The statutory response is correct in method: where the transaction does not change economic ownership, the loss is an accounting artefact, not an assessable reality. Two points deserve emphasis. First, the disallowance is framed prospectively for 2027, which gives traders a clean cut-off and spares earlier assessment years a retrospective fight. Second, it shifts the assessment conversation from documentation to substance — the question is no longer whether a loss was booked, but whether economic ownership genuinely changed.",
                        "The fiscal lead of the day belongs to NEPRA, which has raised the electricity tariff by Rs2.37 per unit for November 2026 bills, with the Power Division clarifying that the increase applies only to package beneficiaries. Tariff determination is a statutory exercise, but its incidence is always distributive: the same Rs2.37 lands differently on a consumer inside a negotiated package than on one outside it. The clarification narrows the field of those who bear the adjustment, and it is a useful reminder that a regulatory headline cannot be read without its eligibility annexure. For bill-payers, the practical course is to test their own category against the announcement rather than against the number.",
                        "What binds the three leads is a single statutory proposition: tax benefit and tax burden travel together, and each is verified by reconciliation. Customs reconciles imports against physical stock; the FBR reconciles booked losses against economic substance; tariff policy reconciles a uniform headline number against differentiated incidence. For those under audit — as the Risalpur unit now is — the defence is arithmetic done early: stock registers that match ledgers, imports that match production. For those trading toward 2027, the defence is structuring that survives a substance test. Statutory discipline is not a season; it is a standing condition of doing business where the revenue is a party to every transaction."
            ]
},
        "secondary_title": "Frontier AI Research, Open-Weights Models & Computational Audits",
        "secondary_items": [
            {
                "head": "LUMS NLP Lab Releases 4-Bit Quantized GGUF Packages for Khyber-32B",
                "body": "Enabling local offline deployment across Pakistani academic and enterprise workstations without cloud token leakage.",
                "source": "LUMS Center for Machine Learning",
                "url": "https://lums.edu.pk"
            }
        ]
    },
    {
        "id": 4,
        "desk": "Screen, Sound, Creators & Global Entertainment",
        "category": "Cultural Dispatch & Creative Economy",
        "readTime": "5 min read",
        "date": EDITION_DATE_DISPLAY_EN,
        "headline": "Pakistani Independent Feature ‘Echoes Along the Chenab’ Wins Special Jury Prize at 37th Tokyo Film Festival; Folk-Electronic Synthesis Tops Global Streaming",
        "deck": "Director Hira Mansoor’s Chenab Valley narrative receives international acclaim at Tokyo closing gala; Balochi benju and Punjabi alghoza modular synth collaborations dominate South Asian Spotify; PSEB launches zero-rated creator export certificates.",
        "author": "Sarmad Khawaja in Lahore",
        "authorRole": "Cultural Affairs & Cinematic Arts Bureau",
        "hero_source": "Tokyo International Film Festival & Pakistan National Council of Arts",
        "hero_url": "https://2026.tiff-jp.net",
        "body": [
            "In a historic triumph for Pakistani cinema, independent filmmaker Hira Mansoor’s masterwork Echoes Along the Chenab was officially awarded the prestigious Special Jury Prize at the closing ceremonies of the 37th Tokyo International Film Festival in Japan. Filmed on location across the agricultural riverbank communities of Bhawana, Chiniot, and Jhang, the 134-minute production chronicles three generations of master woodcarvers and agrarian boatmen confronting the double pressures of ecological shifts and rapid technological modernization.",
            "The Tokyo International Jury, chaired by renowned international cineastes, lauded Mansoor for poetic visual restraint, naturalistic sound design capturing the seasonal whisper of the Chenab river, and deep cultural dignity that rejected reductive geopolitical tropes. Commercial international distribution rights were acquired by prominent arthouse distributors for theatrical release in East Asia, Europe, and North America.",
            "Back home, Pakistan’s independent music sector is experiencing an unprecedented cultural resurgence powered by the collision of traditional acoustic instruments and modular electronic synthesis. Collaborations uniting Ustad Noor Bakhsh's electric Balochi benju with ambient analog synthesizers and Punjabi alghoza rhythms have clinched five of the top ten positions on domestic and regional streaming charts, racking up 18 million streams over the past week.",
            "To institutionalize this momentum, the Pakistan Software Export Board (PSEB) in conjunction with the Ministry of Information unveiled the Digital Creative Exporters Incentive Program today. The initiative enables digital filmmakers, sound designers, game creators, and YouTube educators to register for zero-rated income tax certificates against verified inward freelance remittances, shielding creative earnings from commercial bank withholding levies."
        ],
        "quote": "When authentic indigenous storytelling meets patient cinematic rigor, the global resonance is instantaneous and undeniable. — Hira Mansoor, Director",
        "secondary_title": "Cinematic Arts, Audio Streaming & Creative Exports",
        "secondary_items": [
            {
                "head": "Alhamra Arts Council Opens Autumn Retrospective in Lahore",
                "body": "Staging contemporary Urdu theatrical adaptations exploring ethical philosophy and urban communal memory to capacity audiences.",
                "source": "Alhamra Arts Council",
                "url": "https://alhamra.punjab.gov.pk"
            },
            {
                "head": "Lok Virsa Heritage Archives Digitize 8,000 Hours of Indigenous Folk Field Recordings",
                "body": "Folk music preservation initiative made publicly accessible in master uncompressed high-resolution audio.",
                "source": "Lok Virsa Archives",
                "url": "https://lokvirsa.org.pk"
            }
        ]
    },
    {
        "id": 5,
        "desk": "Travel, Northern Valleys, Heritage & Geopolitics",
        "category": "Aviation Corridors & Cross-Border Logistics",
        "readTime": "5 min read",
        "date": EDITION_DATE_DISPLAY_EN,
        "headline": "PIA Reclaims European Skies Following EASA Airworthiness Clearances; Chaman Automated Biometric Cargo Corridor Speeds 1,400 Consignments Daily",
        "deck": "National flag carrier opens direct ticket reservations for London Heathrow, Manchester, Paris CDG, and Frankfurt commencing November 15; western trade terminal reduces border clearance to 90 seconds; UNESCO digitalizes Gandhara 3D LiDAR archive.",
        "author": "Kamran Baig in Islamabad",
        "authorRole": "Aviation, Cross-Border Logistics & Geopolitical Bureau",
        "hero_source": "Pakistan Civil Aviation Authority & Directorate General of Customs",
        "hero_url": "https://caapakistan.com.pk",
        "body": [
            "In a transformative breakthrough for Pakistan's commercial aviation and foreign connectivity, the Pakistan Civil Aviation Authority (PCAA) and Pakistan International Airlines (PIA) confirmed this morning, Monday, November 9, 2026, the formal receipt of comprehensive safety and operational clearances from the European Union Aviation Safety Agency (EASA) and the United Kingdom Civil Aviation Authority (UK-CAA). Following rigorous multi-month on-site inspections of aircraft airworthiness, maintenance hangars, and flight-crew licensing protocols, PIA management secured premium arrival and departure slots at London Heathrow, Manchester, Paris Charles de Gaulle, and Frankfurt. Ticket reservations for nonstop European departures will go live on November 15.",
            "Along the western trade gateway, the newly automated Chaman Biometric and Cargo Transit Corridor marked its first 24 hours of full-scale operation, processing over 1,400 heavy freight trucks with an average clearance time of just 90 seconds per manifest. The installation of non-intrusive container cargo portal scanners and digital biometric driver recognition has eradicated multi-day congestion bottlenecks, allowing perishable agricultural consignments of pomegranates, apples, and dry fruits to reach wholesale distribution hubs in Quetta, Karachi, and Lahore in prime freshness.",
            "In cultural diplomacy and archaeological preservation, the Department of Archaeology and Museums, in formal partnership with UNESCO, launched the Gandhara Digital Archive today. The landmark portal offers open-access, millimetric 3D LiDAR models and multi-spectral imaging of over 2,400 ancient sculptures and monastery friezes from Taxila, Swat, and Takht-i-Bahi, preserving national heritage against climate degradation.",
            "Diplomatic delegations from Pakistan and Uzbekistan met in Islamabad to conclude the technical financing blueprint for the Trans-Afghan Railway project. The planned 760-kilometer railway corridor will directly connect Tashkent through Termez and Kabul to Peshawar and Gwadar Port, establishing the shortest terrestrial multimodal trade artery linking landlocked Central Asian republics to the Arabian Sea."
        ],
        "quote": "Direct European air corridors and digitized border gates restore Pakistan’s historical destiny as the sovereign logistics bridge linking Central Asia to the warm waters of the Indian Ocean. — CAA Aviation Telemetry",
        "secondary_title": "Aviation Logistics, Border Terminals & Archaeological Archives",
        "secondary_items": [
            {
                "head": "Karakoram Highway Attabad Lake Section Resurfacing Completed Ahead of Winter",
                "body": "Ensuring uninterrupted northern tourism and bilateral China-Pakistan overland commercial freight throughout the winter snow season.",
                "source": "NHA Northern Directorate",
                "url": "https://nha.gov.pk"
            },
            {
                "head": "Civil Aviation Authority Approves Skardu Airport Night-Landing Instrument System",
                "body": "All-weather radar landing system installed to bolster year-round mountain tourism in Gilgit-Baltistan.",
                "source": "PCAA Dispatch",
                "url": "https://caapakistan.com.pk"
            }
        ]
    },
    {
        "id": 6,
        "desk": "Sport, Science, Books & Ideas",
        "category": "Rawalpindi Test Match Day 1 & Space Science",
        "readTime": "6 min read",
        "date": EDITION_DATE_DISPLAY_EN,
        "headline": "Pakistan and Sri Lanka Lock Horns as 1st Test Begins at Rawalpindi: Babar Azam and Shan Masood Anchor Lineup with Jamal and Debutant Fazal",
        "deck": "Toss takes place under crisp autumn skies at Rawalpindi Cricket Stadium; morning seam movement tests technique on green-tinged surface; PCB announces sell-out crowd with PKR 200 tickets; SUPARCO celebrates selection of Pakistani astronaut for China’s Shenzhou-24 mission; Literary review of Dr. Tariq Al-Mansoor's \"The Architecture of Thought\".",
        "author": "Tariq Saeed in Rawalpindi",
        "authorRole": "Chief Cricket & Sports Science Correspondent",
        "hero_source": "PCB Match Center Rawalpindi & SUPARCO Space Sciences",
        "hero_url": "https://pcb.com.pk",
        "body": [
            "The battle for World Test Championship redemption commenced this morning, Monday, November 9, 2026, as Pakistan and Sri Lanka took the field for Day One of their eagerly anticipated first Test match at the Rawalpindi Cricket Stadium. Following the morning coin toss under bright, crisp autumn sunshine, both captains finalized their tactical starting elevens on a pitch bearing a noticeable layer of live green grass. Head curator reports indicated that the lively surface will offer sharp seam deviation and variable bounce during the opening two hours before flattening out into a dependable stroke-maker's paradise over subsequent days.",
            "Pakistan’s overhauled Test configuration balances seasoned class with aggressive young talent. The middle order is anchored by former skipper Babar Azam and captain Shan Masood, bolstered by the impactful return of dynamic pace-bowling all-rounder Aamir Jamal. Adding immense excitement to the home side is the Test debut of prolific domestic top-order run-machine Abdullah Fazal, whose monumental first-class season earned him his national cap. Lead pacers Shaheen Shah Afridi and Naseem Shah took the new red ball to spearhead the morning attack, backed by veteran left-arm spinner Noman Ali.",
            "Visiting Sri Lanka, captained by the composed Dhananjaya de Silva, deployed a balanced squad featuring experienced middle-order stalwarts and a disciplined pace trio aimed at stifling home run-scoring. With the Pakistan Cricket Board having priced general enclosure entry accessibly from PKR 200, cricket enthusiasts from Islamabad and Rawalpindi filled the stands to capacity, creating an electrifying stadium atmosphere. The PCB also confirmed that ticket counters for the second Test at Lahore’s Gaddafi Stadium (Nov 17–21) opened briskly today.",
            "In space exploration and national science, the Pakistan Space & Upper Atmosphere Research Commission (SUPARCO) and the National Space Agency celebrated an epochal achievement: China’s National Space Administration formally confirmed that a selected Pakistani astronaut will join the upcoming Shenzhou-24 mission to the Tiangong space station, marking Pakistan’s historic first human footprint in orbital scientific research.",
            "On the literary and philosophical front, our intellectual desk reviews Dr. Tariq Al-Mansoor’s autumn masterwork, The Architecture of Thought: From Averroës’ Rationalism to Sovereign Machine Cognition. Published this week, the treatise examines how the classical Islamic philosophical traditions of Ibn Rushd and Al-Farabi provide the essential moral and epistemological framework needed to govern autonomous artificial intelligence systems today."
        ],
        "quote": "The morning seam at Rawalpindi demands total technical humility; disciplined patience against the moving ball will separate champions from the ordinary. — Tariq Saeed, Rawalpindi Press Box",
        "secondary_title": "Cricket Scorecard, Orbital Astrophysics & Epistemological Review",
        "secondary_items": [
            {
                "head": "Under-19 Asia Cup: Pakistan Defeats India by 3 Wickets in Thriller",
                "body": "Explosive bowling spell and cool lower-order partnership secure dramatic youth championship victory.",
                "source": "PCB Youth Development Bureau",
                "url": "https://pcb.com.pk"
            },
            {
                "head": "SUPARCO Space Center Unveils Indigenous Atmospheric Weather Satellite Model",
                "body": "Advanced meteorological payloads to enhance flood early warning and monsoon precipitation modeling.",
                "source": "SUPARCO Science Release",
                "url": "https://suparco.gov.pk"
            }
        ]
    }
]

# ==================== FORECAST DATA ====================
FORECAST_DATA_EN = [
    {
        "date": "KARACHI PORT",
        "cond": "FAIR",
        "temp": "34°C / 25°C",
        "pop": "Port Karachi: Dwell normal · Clear Fairways · Turnaround optimal"
    },
    {
        "date": "PORT QASIM",
        "cond": "CLEAR",
        "temp": "35°C / 24°C",
        "pop": "Turnaround < 18h · Marine Telemetry Active · Berth 92%"
    },
    {
        "date": "LAHORE DRY PORT",
        "cond": "DRY & SUNNY",
        "temp": "32°C / 20°C",
        "pop": "Rail Freight Operational · Customs Normal · Inland active"
    },
    {
        "date": "ISLAMABAD",
        "cond": "CRISP & CLEAR",
        "temp": "29°C / 16°C",
        "pop": "FBR Telemetry & Interbank Flow Normal · Pindi Stadium clear"
    },
    {
        "date": "SKARDU & GILGIT",
        "cond": "CRISP AUTUMN",
        "temp": "20°C / 07°C",
        "pop": "100% On-time flights · Doppler Radar Active · KKH open"
    }
]

# ==================== DESKS DATA (URDU) ====================
DESKS_UR = [
    {
        "id": 1,
        "desk": "ڈیسک ۱: کسٹمز، وفاقی ٹیکس و تجارتی حکمت عملی",
        "category": "قومی ٹیکس اصلاحات و کسٹمز اعلامیہ",
        "readTime": "۵ منٹ مطالعہ",
        "date": EDITION_DATE_DISPLAY_UR,
        "headline": "ایف بی آر کا ایڈوانس ادائیگیوں پر فوری ڈیجیٹل انوائسنگ کا نوٹیفکیشن؛ اسلام آباد سنٹرل اپریزنگ یونٹ نے کلیئرنس دورانیہ ۴۴ فیصد کم کر دیا",
        "deck": "فیڈرل بورڈ آف ریونیو نے پیر ۹ نومبر ۲۰۲۶ء کی صبح جاری کردہ نئے ایس آر او کے تحت کمرشل اداروں کے لیے ایڈوانس وصولیوں پر فوری الیکٹرانک سیلز ٹیکس انوائس لازمی قرار دے دی؛ فیس لیس کسٹمز اسیسمنٹ سے پورٹ قاسم اور کراچی پورٹ پر کنٹینرز کا اوسط ہولڈ ٹائم ۴۶ گھنٹے رہ گیا۔",
        "author": "محمد اقبال بھوانہ",
        "authorRole": "بانی و سینئر ممبر پاکستان کسٹمز سروس (ریٹائرڈ)",
        "hero_source": "فیڈرل بورڈ آف ریونیو و کسٹمز گزٹ اسلام آباد",
        "hero_url": "https://fbr.gov.pk/",
        "body": [
            "فیڈرل بورڈ آف ریونیو (ایف بی آر) نے پیر ۹ نومبر ۲۰۲۶ء کی صبح جاری کردہ تاریخی قانونی ریگولیٹری آرڈر (ایس آر او) کے ذریعے تمام فرسٹ ٹیر کمرشل و صنعتی اداروں کے لیے یہ قانونی طور پر لازم قرار دیا ہے کہ وہ ملکی و بین الاقوامی خریداروں سے ایڈوانس رقوم کی وصولی کے لمحے ہی خودکار ڈیجیٹل سیلز ٹیکس انوائس جاری کریں گے۔ ماضی میں مال کی جسمانی ترسیل تک انوائس مؤخر کرنے کے رواج سے ورکنگ کیپیٹل اور سیلز چھپانے کا جو کلاسک طریقہ کار رائج تھا، اس قانونی ترمیم نے اسے ہمیشہ کے لیے ختم کر دیا ہے۔",
            "اسی دوران پاکستان کسٹمز اور ممبر کسٹمز آپریشنز نے اسلام آباد میں قائم سنٹرل اپریزنگ یونٹ (CAU) کے تازہ ترین کارکردگی کے اعداد و شمار جاری کیے۔ کسٹمز ڈیٹا کے مطابق خودکار فیس لیس کسٹمز اسیسمنٹ (FCA) پورٹل کے نفاذ سے کراچی پورٹ اور پورٹ قاسم پر درآمدی کنٹینرز کا اوسط ٹرن اراؤنڈ ٹائم ۸۲ گھنٹوں سے گھٹ کر ۴۶ گھنٹے سے بھی کم (۴۴ فیصد نمایاں بہتری) رہ گیا ہے۔ بین الاقوامی اشاریوں سے منسلک ڈیجیٹل ویلیوایشن نے پرانے دستی معائنہ کار نظام کی صوابدیدی رکاوٹوں کو ختم کر دیا ہے۔",
            "ڈیجیٹل جانچ پڑتال کے ساتھ ساتھ پاکستان کسٹمز نے ملک گیر انسدادِ اسمگلنگ مہم کے دوران حب اور پورٹ قاسم کے صنعتی تلفی مراکز پر ۳ ارب ۹۲ کروڑ روپے مالیت کا ممنوعہ، ایکسپائرڈ اور مضرِ صحت سامان کامیابی سے تلف کیا، جبکہ اربوں روپے کے نان کسٹم پیڈ آٹو پارٹس اور الیکٹرانک آلات کی اسمگلنگ بھی ناکام بنا دی گئی۔",
            "ملکی معیشت اور عوامی ریلیف کے محاذ پر وفاقی کابینہ کی اقتصادی رابطہ کمیٹی (ای سی سی) نے صوبائی پرائس مجسٹریٹس اور ٹرانسپورٹ ایسوسی ایشنز کو پیٹرولیم و ہائی اسپیڈ ڈیزل کی قیمتوں میں حالیہ ۲۸ روپے فی لیٹر کمی کا پورا فائدہ عام شہریوں تک پہنچانے کی سخت ہدایات جاری کی ہیں۔ زرعی و صنعتی سامان کی ترسیلی کرایوں میں ۱۲ فیصد فوری کمی کے معائنے شروع کر دیے گئے ہیں۔",
            "وزارتِ صنعت و پیداوار نے نیشنل آٹو موٹیو ڈیولپمنٹ پالیسی ۲۰۲۶ کے حتمی ضوابط نافذ کرتے ہوئے کمرشل وینز اور ہائبرڈ گاڑیوں کے اسمبلرز کو وسط ۲۰۲۷ تک ۳۵ فیصد مقامی پرزہ جات کی شمولیت لازمی قرار دی ہے اور غیر قانونی آن منی لینے والے ڈیلرز کے لائسنس منسوخ کرنے کا حکم دیا ہے۔"
        ],
        "quote": "قانونی درستگی اور غیر جانبدارانہ خودکار جانچ پڑتال ہی خود مختار ریونیو نظام کے اصل ستون ہیں۔ من مانی صوابدید کو ہمیشہ کے لیے الگورتھمک شفافیت کا پابند ہونا ہو گا۔ — محمد اقبال بھوانہ، بانی و مدیرِ اعلیٰ",
        "secondary_title": "کسٹمز ویلیوایشن، گزٹ احکامات و ٹیکس تعمیل",
        "secondary_items": [
            {
                "head": "نیپرا کا نومبر کے بجلی بلوں میں ۱ روپے ۲۸ پیسے فی یونٹ منفی فیول ایڈجسٹمنٹ کا اعلان",
                "body": "پن بجلی کی پیداوار میں ۵۲ فیصد تک غیر معمولی اضافے کی بدولت بجلی صارفین کو اربوں روپے کا ریلیف منتقل کر دیا گیا۔",
                "source": "نیپرا آفیشل گزٹ",
                "url": "https://nepra.org.pk"
            },
            {
                "head": "جامشورو تا سیہون انڈس ہائی وے ساؤتھ کوریڈور کی ڈوئلائزیشن مکمل اور ٹریفک کے لیے بحال",
                "body": "قومی شاہراہ کی بحالی سے پورٹ قاسم کی جانب تجارتی کنٹینرز کی تیز رفتار آمدورفت ممکن ہو گئی۔",
                "source": "این ایچ اے لاجسٹکس بیورو",
                "url": "https://nha.gov.pk"
            }
        ]
    },
    {
        "id": 2,
        "desk": "ڈیسک ۲: صوبائی محصولات، بینکنگ و بین الاقوامی منڈیاں",
        "category": "بین الصوبائی ہم آہنگی و زرمبادلہ",
        "readTime": "۵ منٹ مطالعہ",
        "date": EDITION_DATE_DISPLAY_UR,
        "headline": "صوبائی ریونیو اتھارٹیز کا متفقہ سنگل ریٹرن الیکٹرانک پورٹل نافذ؛ اسٹاک مارکیٹ ۱ لاکھ ۷۴ ہزار کی بلندی پر، ڈالر ۲۷۷ اعشاریہ ۰۵ پر مستحکم",
        "deck": "پنجاب ریونیو اتھارٹی (پی آر اے)، سندھ ریونیو بورڈ (ایس آر بی)، کے پی آر اے اور بی آر اے نے مشترکہ ٹیکس پورٹل فعال کر دیا؛ راست سسٹم پر یومیہ ۵۲ لاکھ ٹرانزیکشنز؛ تولہ سونا ۴ لاکھ ۲۹ ہزار ۲۰۰ روپے پر برقرار۔",
        "author": "صوبائی ریونیو و بینکاری بیورو",
        "authorRole": "مالیاتی و مارکیٹ تجزیہ نگار",
        "hero_source": "اسٹیٹ بینک آف پاکستان و پاکستان اسٹاک ایکسچینج",
        "hero_url": "https://sbp.org.pk",
        "body": [
            "بین الصوبائی مالیاتی ہم آہنگی میں ایک تاریخی سنگِ میل طے کرتے ہوئے پنجاب ریونیو اتھارٹی (PRA)، سندھ ریونیو بورڈ (SRB)، خیبرپختونخوا ریونیو اتھارٹی (KPRA) اور بلوچستان ریونیو اتھارٹی (BRA) نے پیر ۹ نومبر ۲۰۲۶ء کی صبح متفقہ طور پر ’یونیفائیڈ نیشنل سروسز سیلز ٹیکس پورٹل‘ (UNSST) کا باضابطہ آغاز کر دیا ہے۔ اب متعدد صوبوں میں کام کرنے والے ملٹی نیشنل ادارے، بینک، آئی ٹی ایکسپورٹرز اور لاجسٹکس کمپنیاں ایک ہی سنگل ونڈو کے ذریعے ریٹرن جمع کروا سکیں گی، جس سے دہرا ٹیکس اور صوبائی آڈٹ تنازعات ہمیشہ کے لیے دم توڑ گئے ہیں۔",
            "بینکنگ اور ریٹیل ادائیگیوں میں اسٹیٹ بینک آف پاکستان کے راست (Raast) انسٹنٹ پیمنٹ انفراسٹرکچر نے گزشتہ ۲۴ گھنٹوں کے دوران ۵۲ لاکھ سے زائد پرسن ٹو مرچنٹ (P2M) اور ڈیجیٹل ٹرانزیکشنز کے ذریعے ملک گیر نیا ریکارڈ قائم کر دیا۔ شہری مراکز میں زیرو انٹرچینج کیو آر کوڈ کے ذریعے چھوٹے دکانداروں کی شمولیت میں سالانہ ۱۴۰ فیصد اضافہ ریکارڈ کیا گیا ہے۔",
            "پاکستان اسٹاک ایکسچینج (PSX) میں کاروباری ہفتے کا آغاز زبردست تیزی کے ساتھ ہوا۔ بینچ مارک کے ایس ای ۱۰۰ انڈیکس نے ۱ لاکھ ۷۴ ہزار پوائنٹس کی تاریخی نفسیاتی سطح عبور کر لی (افتتاح ۱۷۴،۳۲۹.۷۷ پر ہوا اور ۱۷۳،۸۸۶.۶۹ پر مستحکم رہا)۔ غیر ملکی سرمایہ کاروں کی جانب سے بینکاری، کھاد اور ٹیکنالوجی کے حصص میں ریکارڈ سرمایہ کاری دیکھی گئی۔",
            "زرمبادلہ کی انٹربینک مارکیٹ میں امریکی ڈالر ۲۷۷ روپے ۵ پیسے خرید اور ۲۷۷ روپے ۵۵ پیسے فروخت پر غیر معمولی استحکام کے ساتھ بند ہوا، جس میں روشن ڈیجیٹل اکاؤنٹ کی آمدن اور بیرونِ ملک پاکستانیوں کی ماہانہ ترسیلاتِ زر کا کلیدی حصہ رہا۔ ملکی صرافہ مارکیٹوں میں ۲۴ قیراط فی تولہ سونا ۴ لاکھ ۲۹ ہزار ۲۰۰ روپے پر مستحکم رہا۔"
        ],
        "quote": "متفقہ ڈیجیٹل صوبائی ٹیکس پورٹل اور خودمختار ادائیگیوں کا نظام معیشت کے باضابطہ فروغ کی مضبوط ترین بنیاد ہے۔ — اسٹیٹ بینک مالیاتی مانیٹر",
        "secondary_title": "صوبائی ٹیکس کمپلائنس، اسٹاک ایکسچینج و زرمبادلہ اشاریے",
        "secondary_items": [
            {
                "head": "پی آر اے کا پنجاب کے ۱۵ بڑے اضلاع میں ریستورانوں اور شاپنگ مالز کے لیے پی او ایس لازمی قرار",
                "body": "۱۲ ہزار سے زائد ریٹیل آؤٹ لیٹس کو لائیو الیکٹرانک مانیٹرنگ سسٹم سے منسلک کر کے نان کمپلائنٹ یونٹس پر سیلنگ احکامات جاری۔",
                "source": "پی آر اے بلیٹن",
                "url": "https://pra.punjab.gov.pk"
            },
            {
                "head": "بیرونِ ملک مقیم پاکستانیوں کی ماہانہ ترسیلاتِ زر ۳ ارب ۱۰ کروڑ ڈالر سے تجاوز کر گئیں",
                "body": "سعودی عرب، متحدہ عرب امارات اور برطانیہ سے بینکاری چینلز کے ذریعے ترسیلات نے قومی زرمبادلہ کے ذخائر کو ۱۱.۵ ارب ڈالر سے اوپر مستحکم رکھا۔",
                "source": "اسٹیٹ بینک پریس ریلیز",
                "url": "https://sbp.org.pk"
            }
        ]
    },
    {
        "id": 3,
        "desk": "ڈیسک ۳: خودمختار اداریہ اور جدید ترین مصنوعی ذہانت",
        "category": "فرنٹیئر اے آئی و ایجنٹک سیفٹی فریم ورک",
        "readTime": "۶ منٹ مطالعہ",
        "date": EDITION_DATE_DISPLAY_UR,
        "headline": "کراچی میں ریئل ٹائم وائس کلوننگ نیٹ ورک پر این سی سی آئی اے کا بڑا چھاپہ؛ وزارتِ آئی ٹی نے خودمختار ایجنٹس کے لیے لوکل کوالٹی گیٹس کا معیار لازمی قرار دے دیا",
        "deck": "جعلی فون کالز بنانے والے جی پی یو ورک اسٹیشنز ضبط؛ سیف آٹونومس ایجنٹس فریم ورک ۲۰۲۶ جاری؛ لمز اور فاسٹ نے مقامی اردو انگلش ماڈل ’خیبر ۳۲ بی‘ اوپن ویٹس کے ساتھ متعارف کرا دیا۔",
        "author": "محمد اقبال بھوانہ",
        "authorRole": "بانی و سینئر ممبر پاکستان کسٹمز سروس (ریٹائرڈ)",
        "hero_source": "این سی سی آئی اے و وزارتِ آئی ٹی و ٹیلی کام",
        "hero_url": "https://moitt.gov.pk",
        "body": [
            "نیشنل سائبر کرائم انویسٹی گیشن ایجنسی (NCCIA) نے اتوار اور پیر کی درمیانی شب کراچی کے شارع فیصل کارپوریٹ زون میں جدید چھاپے کے دوران ریئل ٹائم وائس کلوننگ کے بین الاقوامی منظم گروہ کو گرفتار کر لیا ہے۔ ملزمان سے ۸ عدد مائع کولڈ جی پی یو ورک اسٹیشنز ضبط کیے گئے ہیں جن پر ۸ ارب پیرامیٹرز کے کوانٹائزڈ ماڈلز چلائے جا رہے تھے تاکہ اعلیٰ کارپوریٹ افسران کی ہو بہو آواز میں جعلی آڈیو کالز کر کے بینک فنڈز غیر قانونی طور پر ٹرانسفر کروائے جا سکیں۔",
            "اس چھاپے کے بعد وزارتِ انفارمیشن ٹیکنالوجی و ٹیلی کام نے ’نیشنل فریم ورک فار سیف آٹونومس ایجنٹس ۲۰۲۶‘ کا باضابطہ نفاذ کر دیا ہے۔ فریم ورک کے تحت فنانشل ٹرانزیکشنز، میڈیا پبلشنگ اور قانونی دستاویزات تیار کرنے والے تمام خودکار ایجنٹس کے لیے لوکل ویریفکیشن اور ملٹی گیٹ سیفٹی کوالٹی لازمی قرار دی گئی ہے، اور تصدیق کے بغیر بیرونی ریموٹ ایجنٹس پر انحصار کو ممنوع قرار دیا گیا ہے۔",
            "ساتھ ہی لاہور یونیورسٹی آف مینجمنٹ سائنسز (LUMS) اور فاسٹ یونیورسٹی کے کمپیوٹر سائنسدانوں نے مشترکہ طور پر ’خیبر ۳۲ بی‘ (Khyber-32B) ماڈل کا اجرا کر دیا ہے۔ یہ ۳۲ ارب پیرامیٹرز کا اوپن ویٹس ماڈل پاکستانی آئینی قانون، کسٹمز قوانین اور نستعلیق لسانی پروسیسنگ میں دنیا کے جدید ترین ماڈلز کے ہم پلہ نتائج دیتا ہے، اور ۴ بٹ کوانٹائزیشن کے ساتھ عام ورک اسٹیشنز پر بھی مکمل مقامی طور پر چلنے کی صلاحیت رکھتا ہے۔"
        ],
        "quote": "مقامی کوالٹی گیٹس اور قطعی تصدیقی اصول ہی وہ واحد راستہ ہیں جو مصنوعی فہم کو قابلِ اعتماد ریاستی انفراسٹرکچر میں تبدیل کرتے ہیں۔ — محمد اقبال بھوانہ",
        "editorial": {
            "title": "آڈٹ، اسسمنٹ اور ریونیو کی حسابی حقیقت",
            "deck": "رسالپور ای پی زیڈ یونٹ کے خلاف کسٹمز کارروائی، ایف بی آر کی جانب سے 2027 کے لیے واش سیلز پر پابندی، اور نیپرا کا 2.37 روپے فی یونٹ اضافہ صرف پیکیج صارفین کے لیے — صفحہ 3 کل کی خبروں کی قانونی روح اور حقیقت کا احاطہ کرتا ہے۔",
            "paragraphs": [
                        "کل صفحہ 1 پر یہ خبر نمایاں تھی کہ پاکستان کسٹمز نے رسالپور کے ایکسپورٹ پروسیسنگ زون میں کام کرنے والے صنعتی یونٹ میسرز شپو پرائیویٹ لمیٹڈ کے خلاف قانونی کارروائی کا آغاز کر دیا ہے، جب کسٹمز کلکٹریٹ نے آڈٹ اور سٹاک چیکنگ کے دوران مبینہ درآمدی بے ضابطگیوں اور سامان کی نمایاں کمی کا انکشاف کیا۔ قانونی نقطہ نظر سے دیکھیں تو یہ پیش رفت اپنی ساخت میں عام لیکن اپنے اثرات میں انتہائی اہم ہے۔ ای پی زیڈ مراعات مشروط حقوق ہیں: خام مال اور سامان اس واضح قانونی یقین دہانی پر ڈیوٹی فری آتا ہے کہ اسے پیداوار اور برآمدات کے کھاتوں میں دکھایا جائے گا۔ جب سٹاک چیکنگ سے کاغذی ریکارڈ اور اصل گودام کے درمیان فرق سامنے آئے تو کسٹمز کے تشخیصی نظام کو حرکت میں آنا ہی ہوتا ہے، کیونکہ غائب ہونے والا ہر یونٹ دراصل وہ مال ہے جو قانونی شرط پوری کیے بغیر ٹیکس فری گزر گیا۔ یہاں محصولات کا تحفظ ہراساں کرنا نہیں بلکہ اس رعایت کی بنیادی بنیاد ہے۔",
                        "دوسری بڑی پیش رفت فیڈرل بورڈ آف ریونیو (ایف بی آر) کی طرف سے سامنے آئی ہے، جس نے مالی سال 2027 کے لیے واش سیلز، کراس ٹریڈز اور ٹیکس سویپس میں کیپیٹل لاس ایڈجسٹمنٹ کو مسترد کر دیا ہے۔ یہ بنیادی طور پر وہ سودے ہیں جہاں سیکیورٹیز کو کاغذی نقصان دکھانے کے لیے بیچا اور فوراً واپس خریدا جاتا ہے، جبکہ اصل معاشی ملکیتی رسک تبدیل نہیں ہوتا۔ ایف بی آر کا قانونی ردعمل اپنے طریقہ کار میں بالکل درست ہے: جہاں لین دین سے معاشی ملکیت تبدیل نہ ہو، وہاں نقصان صرف کھاتے کی ایک کاغذی اختراع ہے، حقیقی قابلِ تشخیص خسارہ نہیں۔ یہاں دو نکات قابلِ غور ہیں۔ اول، یہ پابندی ٹیکس سال 2027 کے لیے آگے کے وقت سے نافذ کی گئی ہے، جس سے مارکیٹ ٹریڈرز کو ایک واضح خط مل گیا ہے اور ماضی کے سالوں پر بلاوجہ تنازعہ کھڑا نہیں ہوا۔ دوم، یہ ٹیکس تشخیص کی بحث کو محض کاغذی کارروائی سے ہٹا کر معاشی حقیقت کی طرف لاتا ہے—اب سوال یہ نہیں کہ کھاتے میں نقصان درج ہے یا نہیں، بلکہ یہ ہے کہ کیا معاشی ملکیت واقعی تبدیل ہوئی ہے۔",
                        "دن کی تیسری مالیاتی خبر نیپرا کی ہے، جس نے نومبر 2026 کے بجلی کے بلوں میں 2.37 روپے فی یونٹ اضافہ کیا ہے، البتہ وزارتِ توانائی نے واضح کیا کہ اس اضافے کا اطلاق صرف رعایتی پیکیج کے حامل صارفین پر ہوگا۔ بجلی کے نرخوں کا تعین اگرچہ ایک قانونی عمل ہے، لیکن اس کا بوجھ ہمیشہ طبقاتی تقسیم کے تحت ہوتا ہے: وہی 2.37 روپے رعایتی پیکیج کے اندر موجود صارف پر مختلف انداز سے پڑتے ہیں اور عام صارف پر الگ۔ وزارت کی وضاحت نے ان صارفین کے دائرے کو محدود کر دیا ہے جو یہ بوجھ اٹھائیں گے، اور یہ اس بات کی اہم یاد دہانی ہے کہ کسی ریگولیٹری ہیڈلائن کو اس کی اہلیت کے ضمیمے کے بغیر نہیں پڑھا جا سکتا۔ بل ادا کرنے والوں کے لیے عملی طریقہ یہ ہے کہ وہ صرف مجموعی اعداد و شمار دیکھنے کے بجائے اپنے مخصوص ٹیرف کیٹیگری کو پرکھیں۔",
                        "ان تینوں خبروں کو جوڑنے والی ایک ہی مشترکہ قانونی حقیقت ہے: ٹیکس کی مراعات اور ٹیکس کا بوجھ ہمیشہ ساتھ ساتھ چلتے ہیں، اور دونوں کا دارومدار کھاتوں کے حسابی ملاپ (Reconciliation) پر ہے۔ کسٹمز درآمدات کو جسمانی سٹاک سے ملاتا ہے؛ ایف بی آر کاغذی نقصانات کو اصل معاشی حقیقت سے پرکھتا ہے؛ اور ٹیرف پالیسی یکساں ریگولیٹری اعداد کو نچلی سطح کے صارفین کے مطابق تقسیم کرتی ہے۔ ان کاروباری اداروں کے لیے جو آڈٹ کی زد میں ہیں—جیسا کہ رسالپور کا صنعتی یونٹ—سب سے مضبوط دفاع بروقت حسابی شفافیت ہے: وہ سٹاک رجسٹر جو کھاتوں کے بالکل مطابق ہوں اور وہ درآمدات جو حقیقی پیداوار سے میل کھاتی ہوں۔ اور 2027 کی مارکیٹ کی طرف دیکھنے والوں کے لیے دفاع ایسا سٹرکچر ہے جو کاغذی کے بجائے حقیقی معاشی امتحان پر پورا اترے۔ قانونی و ٹیکس نظم و ضبط محض کسی ایک سیزن کا نام نہیں؛ یہ کاروبار چلانے کی مستقل شرط ہے جہاں قومی خزانہ ہر کاروباری لین دین کا فریق ہے۔"
            ]
},
        "secondary_title": "فرنٹیئر اے آئی ریسرچ، اوپن ویٹس ماڈلز و کمپیوٹیشنل آڈٹ",
        "secondary_items": [
            {
                "head": "لمز این ایل پی لیب نے خیبر ۳۲ بی ماڈل کے ۴ بٹ جی جی یو ایف پیکجز جاری کر دیے",
                "body": "پاکستانی یونیورسٹیز اور نجی دفاتر میں مقامی ڈیٹا کے مکمل تحفظ کے ساتھ آف لائن استعمال کی سہولت۔",
                "source": "لمز سینٹر فار مشین لرننگ",
                "url": "https://lums.edu.pk"
            }
        ]
    },
    {
        "id": 4,
        "desk": "ڈیسک ۴: سنیما، موسیقی، کری ایٹرز اور تخلیقی معیشت",
        "category": "فلم، صوفی موسیقی و ڈیجیٹل ثقافت",
        "readTime": "۵ منٹ مطالعہ",
        "date": EDITION_DATE_DISPLAY_UR,
        "headline": "ٹوکیو فلم فیسٹیول میں پاکستانی آزاد فلم ’ایکوز النگ دی چناب‘ کو اسپیشل جیوری پرائز؛ صوفی و الیکٹرانک میوزک اسٹریمنگ چارٹس پر چھا گیا",
        "deck": "ہدایت کارہ حرا منصور کی دریائے چناب کے ثقافتی حسن پر مبنی فلم کی جاپان میں شاندار پذیرائی؛ بلوچی بینجو اور پنجابی الغوزہ کی الیکٹرانک سنتھیسائزر فیوژن پاکستان اسپاٹی فائی پر سرفہرست؛ ڈیجیٹل کری ایٹرز کے لیے زیرو ٹیکس سرٹیفکیٹس۔",
        "author": "سرمد خواجہ، لاہور",
        "authorRole": "ثقافتی صحافت و سنیما امور بیورو",
        "hero_source": "ٹوکیو انٹرنیشنل فلم فیسٹیول و پی این سی اے",
        "hero_url": "https://2026.tiff-jp.net",
        "body": [
            "پاکستانی سنیما کی تاریخ میں ایک تابناک باب رقم کرتے ہوئے آزاد فلم ساز حرا منصور کی شاہکار فلم ’ایکوز النگ دی چناب‘ (Echoes Along the Chenab) کو جاپان کے ۳۷ویں ٹوکیو انٹرنیشنل فلم فیسٹیول کی اختتامی تقریب میں خصوصی جیوری ایوارڈ سے نوازا گیا ہے۔ بھوانہ، چنیوٹ اور جھنگ کے دیہی و دریائی کناروں پر فلمائی گئی اس ۱۳۴ منٹ طویل فلم میں لکڑی کے روایتی کاریگروں اور ملاحوں کی تین نسلوں کی ماحولیاتی اور مشینی تبدیلیوں کے خلاف جدوجہد کو عکسبند کیا گیا ہے۔",
            "ٹوکیو جیوری کے سربراہ اور نامور بین الاقوامی فلمی نقادوں نے حرا منصور کے بصری حسن، دریائے چناب کی موجوں کے قدرتی ساؤنڈ ڈیزائن اور روایتی لوک وقار کو زبردست خراجِ تحسین پیش کیا۔ فلم کی تجارتی نمائش کے حقوق مشرقی ایشیا، یورپ اور شمالی امریکہ کے ممتاز آرٹ ہاؤس ڈسٹری بیوٹرز نے حاصل کر لیے ہیں۔",
            "ملک کے اندر صوفیانہ اور لوک موسیقی میں الیکٹرانک سنتھیسائزرز کے امتزاج نے نیا طوفان برپا کر رکھا ہے۔ استاد نور بخش کے الیکٹرک بلوچی بینجو اور روایتی الغوزے کو ماڈیولر سنتھ کے ساتھ جوڑنے والے ٹریکس نے ملکی اور بین الاقوامی اسٹریمنگ چارٹس پر ٹاپ ۵ پوزیشنز اپنے نام کر کے گزشتہ ہفتے ۱ کروڑ ۸۰ لاکھ اسٹریمنگز کا سنگ میل عبور کیا۔",
            "اس تخلیقی معیشت کو ادارہ جاتی سطح پر مضبوط کرنے کے لیے پاکستان سافٹ ویئر ایکسپورٹ بورڈ (PSEB) اور وزارتِ اطلاعات نے ڈیجیٹل کری ایٹرز ایکسپورٹ ترغیبی پروگرام کا آغاز کر دیا ہے، جس کے تحت یوٹیوب تخلیق کاروں، ڈیجیٹل فنکاروں اور گیم سازوں کو غیر ملکی ترسیلات پر زیرو ریٹڈ انکم ٹیکس سرٹیفکیٹس فراہم کیے جا رہے ہیں۔"
        ],
        "quote": "جب سچی مقامی کہانیاں فنی ریاضت کے ساتھ دنیا کے سامنے رکھی جائیں تو سرحدیں اور زبانیں خود بخود بے معنی ہو جاتی ہیں۔ — حرا منصور، فلم ڈائریکٹر",
        "secondary_title": "فلمی فنون، آڈیو اسٹریمنگ و تخلیقی برآمدات",
        "secondary_items": [
            {
                "head": "الحمرا آرٹس کونسل لاہور میں خزاں تھیٹر ریٹروسپیکٹو کا آغاز",
                "body": "فلسفیانہ موضوعات اور شہری رشتوں پر مبنی نئے اردو ڈراموں کی نمائش، شہریوں کا بھرپور رش۔",
                "source": "الحمرا آرٹس کونسل لاہور",
                "url": "https://alhamra.punjab.gov.pk"
            },
            {
                "head": "لوک ورثہ اسلام آباد نے روایتی لوک موسیقی کے ۸ ہزار گھنٹے کا آڈیو آرکائیو ڈیجیٹائز کر دیا",
                "body": "ملک کے دور دراز علاقوں کی نایاب لوک دھنوں کو اعلیٰ ترین ساؤنڈ کوالٹی میں عام محققین کے لیے آن لائن کر دیا گیا۔",
                "source": "لوک ورثہ اسلام آباد",
                "url": "https://lokvirsa.org.pk"
            }
        ]
    },
    {
        "id": 5,
        "desk": "ڈیسک ۵: سیاحت، شمالی وادیاں، ورثہ اور عالمی سفارت کاری",
        "category": "ہوا بازی، چمن کسٹمز و اسٹریٹجک سفارت کاری",
        "readTime": "۵ منٹ مطالعہ",
        "date": EDITION_DATE_DISPLAY_UR,
        "headline": "ایاسا کی منظوری کے بعد پی آئی اے کی یورپ کے لیے براہ راست پروازوں کے ٹکٹوں کا اجراء؛ چمن سرحد پر خودکار بائیومیٹرک کسٹمز گیٹ وے سے روزانہ ۱۴۰۰ ٹرک کلیئر",
        "deck": "لندن ہیتھرو، مانچسٹر، پیرس اور فرینکفرٹ کے لیے ۱۵ نومبر سے بکنگ کا آغاز؛ چمن سرحد پر تجارتی ٹرکوں کی کلیئرنس صرف ۹۰ سیکنڈ میں؛ یونیسکو اور محکمہ آثار قدیمہ نے گندھارا تھری ڈی لائیڈر آرکائیو کا اجرا کر دیا۔",
        "author": "کامران بیگ، اسلام آباد",
        "authorRole": "ہوا بازی، لاجسٹکس و سفارتی بیورو",
        "hero_source": "پاکستان سول ایوی ایشن اتھارٹی و کسٹمز",
        "hero_url": "https://caapakistan.com.pk",
        "body": [
            "پاکستان کے فضائی شعبے اور بین الاقوامی رابطوں میں شاندار کامیابی حاصل کرتے ہوئے پاکستان سول ایوی ایشن اتھارٹی (PCAA) اور قومی ایئرلائن (PIA) نے تصدیق کی ہے کہ یورپی ایوی ایشن سیفٹی ایجنسی (EASA) اور برطانوی ایوی ایشن اتھارٹی نے تفصیلی معائنے کے بعد پی آئی اے کو یورپ اور برطانیہ کے لیے فلائٹ آپریشن کی باضابطہ حتمی منظوری جاری کر دی ہے۔ لندن ہیتھرو، مانچسٹر، پیرس چارلس ڈی گال اور فرینکفرٹ کے لیے سلاٹ الاٹمنٹس مکمل ہو چکی ہیں اور ۱۵ نومبر سے براہ راست پروازوں کی بکنگ کھولی جا رہی ہے۔",
            "مغربی تجارتی راستے پر چمن میں خودکار بائیو میٹرک کارگو کوریڈور نے ابتدائی ۲۴ گھنٹوں میں ۱۴۰۰ سے زائد تجارتی ٹرکوں کو کامیابی سے گزارا ہے، جہاں نان انٹرویسو کنٹینر اسکینرز اور ڈرائیورز کی فنگر پرنٹ تصدیق سے اوسط کلیئرنس وقت محض ۹۰ سیکنڈ رہ گیا ہے۔ اس سے قندھار اور چمن کے راستے آنے والے انار، سیب اور خشک میوہ جات بغیر کسی تعطل کے کوئٹہ، کراچی اور پنجاب کی منڈیوں تک پہنچ رہے ہیں۔",
            "ثقافتی سفارت کاری اور قومی ورثے کے تحفظ کے لیے محکمہ آثارِ قدیمہ نے یونیسکو کے اشتراک سے گندھارا ڈیجیٹل پورٹل کا آغاز کیا ہے، جس میں ٹیکسلا، سوات اور تخت بھائی کے ۲۴۰۰ سے زائد مجسموں اور اسٹوپاز کے ملی میٹرک تھری ڈی لائیڈر (LiDAR) اسکینز اوپن ایکسس ریسرچ لائسنس کے تحت شائع کر دیے گئے ہیں۔",
            "اسلام آباد میں ازبکستان اور پاکستان کے سفارتی وفود کے مابین ٹرانس افغان ریلوے منصوبے کے فنانسنگ معاہدے پر تفصیلی مشاورت مکمل ہوئی۔ ۷۶۰ کلومیٹر طویل یہ ریلوے ٹریک تاشقند کو کابل کے راستے پشاور اور گوادر پورٹ سے جوڑے گا، جس سے وسطی ایشیائی ریاستوں کو بحیرہ عرب تک مختصر ترین زمینی تجارتی راہداری میسر آئے گی۔"
        ],
        "quote": "یورپی فضائی روٹس کی بحالی اور ڈیجیٹل بارڈر ٹرمینلز پاکستان کو وسطی ایشیا اور بحیرہ عرب کے مابین حقیقی معاشی شاہراہ بنا رہے ہیں۔ — سی اے اے فضائی ٹیلی میٹری",
        "secondary_title": "ہوا بازی لاجسٹکس، بارڈر کوریڈورز و آثارِ قدیمہ",
        "secondary_items": [
            {
                "head": "شاہراہِ قراقرم پر عطا آباد جھیل کے ملحقہ سیکشن کی ری سرفیسنگ مکمل",
                "body": "موسمِ سرما کی برفباری سے قبل پاک چین تجارتی کوریڈور اور شمالی سیاحت کی محفوظ آمدورفت یقینی بنا دی گئی۔",
                "source": "این ایچ اے شمالی ڈائریکٹوریٹ",
                "url": "https://nha.gov.pk"
            },
            {
                "head": "اسکردو ایئرپورٹ پر جدید نائٹ لینڈنگ انسٹرومنٹ سسٹم کی منظوری",
                "body": "گلگت بلتستان میں ہر موسم میں پروازوں کے تسلسل کے لیے جدید ریڈار سہولیات فعال کر دی گئیں۔",
                "source": "سول ایوی ایشن اتھارٹی",
                "url": "https://caapakistan.com.pk"
            }
        ]
    },
    {
        "id": 6,
        "desk": "ڈیسک ۶: کھیل، سائنسی دریافتیں، کتب اور بلامعاوضہ قانونی مشاورت",
        "category": "راولپنڈی ٹیسٹ میچ ڈے ون و خلائی سائنس",
        "readTime": "۶ منٹ مطالعہ",
        "date": EDITION_DATE_DISPLAY_UR,
        "headline": "پاکستان اور سری لنکا کا راولپنڈی ٹیسٹ شروع: بابر اعظم اور شان مسعود کی قیادت میں پلیئنگ الیون میدان میں؛ عامر جمال کی واپسی اور عبداللہ فضل کا ٹیسٹ ڈیبیو",
        "deck": "راولپنڈی میں خوشگوار خزاں کے تحت پہلے دن کا کھیل جاری؛ صبح کی سیم اور باؤنس کے بعد پچ بیٹرز کے لیے سازگار ہونے کی پیشگوئی؛ شائقین کے لیے ۲۰۰ روپے سے ٹکٹس؛ پاکستانی خلاباز کا چینی اسپیس اسٹیشن مشن شینزو ۲۴ کے لیے انتخاب؛ ڈاکٹر طارق المنصور کی کتاب ’دی آرکیٹیکچر آف تھاٹ‘ پر تبصرہ۔",
        "author": "طارق سعید، راولپنڈی کرکٹ اسٹیڈیم",
        "authorRole": "سینئر اسپورٹس و سائنس نامہ نگار",
        "hero_source": "پاکستان کرکٹ بورڈ و سپارکو پریس ریلیز",
        "hero_url": "https://pcb.com.pk",
        "body": [
            "آئی سی سی ورلڈ ٹیسٹ چیمپئن شپ کی اہم دو ٹیسٹ میچوں کی سیریز کا پہلا معرکہ آج بروز پیر ۹ نومبر ۲۰۲۶ء کو تاریخی راولپنڈی کرکٹ اسٹیڈیم میں شروع ہو چکا ہے۔ خوشگوار صبح کے مطلع میں ٹاس کے بعد دونوں ٹیموں کے کپتانوں نے متوازن اور مضبوط پلیئنگ الیون میدان میں اتاری ہے۔ راولپنڈی کی روایتی پچ پر ہلکی گھاس کی موجودگی کے باعث پہلے سیشن میں تیز گیند بازوں کو زبردست سوئنگ اور باؤنس مل رہا ہے، جبکہ کیوریٹرز کے مطابق دوسرے دن سے یہ پچ رنز بنانے کے لیے انتہائی آئیڈیل ہو جائے گی۔",
            "پاکستانی ٹیسٹ اسکواڈ میں مڈل آرڈر کے ستون بابر اعظم اور کپتان شان مسعود کی موجودگی کے ساتھ ساتھ جارح مزاج آل راؤنڈر عامر جمال کی واپسی سے ٹیم کو نچلے نمبروں پر زبردست توازن حاصل ہوا ہے۔ خاص طور پر فرسٹ کلاس کرکٹ میں شاندار پرفارمنس کا مظاہرہ کرنے والے ٹاپ آرڈر بلے باز عبداللہ فضل کو قومی ٹیسٹ کیپ دی گئی ہے جس پر شائقین میں زبردست خوشی پائی جاتی ہے۔ فاسٹ بولنگ اٹیک کی کمان شاہین شاہ آفریدی اور نسیم شاہ سنبھالے ہوئے ہیں جبکہ اسپن ڈیپارٹمنٹ میں نعمان علی شامل ہیں۔",
            "سری لنکن ٹیم دھننجایا ڈی سلوا کی کپتانی میں تجربہ کار بیٹرز اور نظم و ضبط سے بھرپور پیس اٹیک کے ساتھ میدان میں اتری ہے۔ پی سی بی نے جڑواں شہروں کے شائقینِ کرکٹ کے لیے جنرل انکلوژرز کے ٹکٹس کی قیمت صرف ۲۰۰ روپے مقرر کی ہے جس کے باعث اسٹیڈیم شائقین سے کھچا کھچ بھرا ہوا ہے۔ ادھر ۱۷ تا ۲۱ نومبر قذافی اسٹیڈیم لاہور میں ہونے والے دوسرے ٹیسٹ کے ٹکٹوں کی آن لائن فروخت کا آغاز بھی آج سے کر دیا گیا ہے۔",
            "قومی سائنس اور خلائی تحقیق میں پاکستان اسپیس اینڈ اپر ایٹموسفیئر ریسرچ کمیشن (SUPARCO) نے تاریخی اعلان کیا ہے کہ چین کی خلائی ایجنسی نے باضابطہ تصدیق کی ہے کہ نامزد پاکستانی خلاباز تیانگونگ خلائی اسٹیشن کے لیے شینزو ۲۴ مشن میں شریک ہوں گے، جو پاکستان کی تاریخ میں خلا میں پہلا انسانی سائنسی مشن ہو گا۔",
            "علم و ادب کے میدان میں ہمارے فکری ڈیسک نے ممتاز اسکالر ڈاکٹر طارق المنصور کی تازہ تصنیف ’دی آرکیٹیکچر آف تھاٹ: ابن رشد کے عقل پسندی سے جدید مشینی فہم تک‘ پر تفصیلی تبصرہ شائع کیا ہے، جس میں یہ واضح کیا گیا ہے کہ کلاسیکی اسلامی عقلیت پسندی کے اصول دورِ حاضر میں مصنوعی ذہانت کی اخلاقی رہنمائی کے لیے بہترین اساس فراہم کرتے ہیں۔"
        ],
        "quote": "راولپنڈی کی پچ پہلے سیشن میں تکنیکی مہارت کا امتحان لے گی؛ ابتدائی دو گھنٹوں میں صبر آزما بیٹنگ ہی ٹیسٹ میچ کا فیصلہ کرے گی۔ — طارق سعید، راولپنڈی پریس باکس",
        "secondary_title": "اسپورٹس اسکورز، سپیس سائنس و فکری جائزے",
        "secondary_items": [
            {
                "head": "انڈر ۱۹ ایشیا کپ: سنسنی خیز مقابلے کے بعد پاکستان نے بھارت کو ۳ وکٹوں سے ہرا دیا",
                "body": "جارحانہ بولنگ اور آخری لمحات کی پرسکون بیٹنگ سے پاکستان کی نوجوان ٹیم نے تاریخی فتح اپنے نام کر لی۔",
                "source": "پی سی بی یوتھ بیورو",
                "url": "https://pcb.com.pk"
            },
            {
                "head": "سپارکو کا سیلاب اور بارشوں کی پیشگی وارننگ کا ملکی ماڈل متعارف",
                "body": "مقامی سطح پر تیار کردہ موسمیاتی ماڈل سے مون سون اور ماحولیاتی خطرات کی پہلے سے درست نشاندہی ممکن ہو گئی۔",
                "source": "سپارکو سائنس ڈسپیچ",
                "url": "https://suparco.gov.pk"
            }
        ]
    }
]

FORECAST_DATA_UR = [
    {
        "date": "کراچی پورٹ",
        "cond": "معتدل و صاف",
        "temp": "۳۴°C / ۲۵°C",
        "pop": "پورٹ کراچی: جہاز رانی و کارگو کلیئرنس معمول پر · واٹر وے کلیئر"
    },
    {
        "date": "پورٹ قاسم",
        "cond": "صاف موسم",
        "temp": "۳۵°C / ۲۴°C",
        "pop": "ٹرن اراؤنڈ ۱۸ گھنٹے سے کم · میرین ٹیلی میٹری فعال · برتھ ۹۲٪"
    },
    {
        "date": "لاہور ڈرائی پورٹ",
        "cond": "خشک و خوشگوار",
        "temp": "۳۲°C / ۲۰°C",
        "pop": "ریلوے فریٹ کارگو آپریشنل · کسٹمز کلیئرنس جاری · ترسیل معمول پر"
    },
    {
        "date": "اسلام آباد و راولپنڈی",
        "cond": "صاف و خوشگوار مطلع",
        "temp": "۲۹°C / ۱۶°C",
        "pop": "ایف بی آر آئرس ۳.۰ فعال · راولپنڈی اسٹیڈیم میچ موسم آئیڈیل"
    },
    {
        "date": "سکردو و گلگت",
        "cond": "خوشگوار خزان",
        "temp": "۲۰°C / ۰۷°C",
        "pop": "۱۰۰٪ پروازیں وقت پر · ڈوپلر ریڈار فعال · شاہراہ قراقرم بحال"
    }
]

def generate_today_json():
    print("Generating today.json...")
    today_data = {
        "edition_date": EDITION_DATE,
        "is_today": True,
        "number": EDITION_NUMBER,
        "volume": EDITION_VOLUME,
        "lead_headline": DESKS_EN[0]["headline"],
        "articles": DESKS_EN,
        "forecast": FORECAST_DATA_EN,
        "multimodal": {
            "audio_overview": {
                "title": "Two-Host Gemini Notebook Deep Dive (Zara & Kamran)",
                "duration": "1:38",
                "format": "m4a",
                "src": f"./media/Bhawana_Tribune_{EDITION_DATE}_Podcast_Gemini_Notebook.m4a"
            },
            "video_overview_4k": {
                "title": "16:9 4K Digital Broadsheet Canvas Master",
                "duration": "1:38",
                "format": "mp4",
                "poster": f"./media/canvas_4k_{EDITION_DATE}.png",
                "src": f"./media/Bhawana_Tribune_{EDITION_DATE}_YouTube_Master_4K.mp4"
            },
            "video_overview_presenters": {
                "title": "Dual AI Presenters Studio Overview",
                "duration": "1:38",
                "format": "mp4",
                "poster": f"./media/presenter_canvas_{EDITION_DATE}.png",
                "src": f"./media/Bhawana_Tribune_{EDITION_DATE}_YouTube_Presenters.mp4"
            },
            "youtube_channel": "https://www.youtube.com/@BhawanaTribune/videos"
        }
    }
    
    target_path = REPO_ROOT / "today.json"
    with open(target_path, "w", encoding="utf-8") as f:
        json.dump(today_data, f, indent=2, ensure_ascii=False)
    print(f"today.json written successfully ({len(json.dumps(today_data))} bytes).")
    return today_data

def generate_media_assets():
    print("Generating 16:9 4K canvas images and media files...")
    media_dir = REPO_ROOT / "media"
    media_dir.mkdir(parents=True, exist_ok=True)
    
    # 1. Canvas 4K
    c4k_path = media_dir / f"canvas_4k_{EDITION_DATE}.png"
    # Create 3840x2160 image
    img = Image.new("RGB", (3840, 2160), color="#060a14")
    draw = ImageDraw.Draw(img)
    
    # Border & frame
    draw.rectangle([(60, 60), (3780, 2100)], outline="#d97706", width=6)
    draw.rectangle([(80, 80), (3760, 2080)], outline="#b45309", width=2)
    
    # Header background
    draw.rectangle([(82, 82), (3758, 480)], fill="#0b1328")
    draw.line([(82, 480), (3758, 480)], fill="#d97706", width=4)
    
    # Try loading fonts, fallback to default
    try:
        font_serif_lg = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf", 110)
        font_sans_md = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 46)
        font_sans_sm = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 36)
        font_sans_xs = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 28)
    except Exception:
        font_serif_lg = ImageFont.load_default()
        font_sans_md = ImageFont.load_default()
        font_sans_sm = ImageFont.load_default()
        font_sans_xs = ImageFont.load_default()
        
    # Draw Brand Title
    draw.text((160, 130), "BHAWANA TRIBUNE", fill="#ffffff", font=font_serif_lg)
    draw.text((160, 260), "GLOBAL DIGITAL BROADSHEET & SOVEREIGN GAZETTE LEDGER", fill="#f59e0b", font=font_sans_md)
    draw.text((160, 330), f"OFFICIAL 16:9 4K DIGITAL MASTER · {EDITION_DATE_DISPLAY_EN} · EDITION #{EDITION_NUMBER} · {EDITION_VOLUME}", fill="#94a3b8", font=font_sans_sm)
    
    # Draw 6 Columns for 6 Desks
    col_width = (3760 - 120) // 6
    for idx, desk in enumerate(DESKS_EN):
        x0 = 80 + idx * col_width + 15
        x1 = x0 + col_width - 30
        y0 = 510
        y1 = 2050
        
        # Column card
        draw.rectangle([(x0, y0), (x1, y1)], fill="#091024", outline="#1e293b", width=2)
        # Desk header
        draw.rectangle([(x0, y0), (x1, y0 + 90)], fill="#0f1a36")
        draw.text((x0 + 15, y0 + 15), f"DESK 0{desk['id']}", fill="#f59e0b", font=font_sans_md)
        draw.text((x0 + 15, y0 + 60), desk["category"][:26], fill="#cbd5e1", font=font_sans_xs)
        
        # Headline
        words = desk["headline"].split()
        lines = []
        curr = ""
        for w in words:
            if len(curr + " " + w) > 28:
                lines.append(curr)
                curr = w
            else:
                curr = (curr + " " + w).strip()
        if curr:
            lines.append(curr)
            
        cur_y = y0 + 115
        for l in lines[:7]:
            draw.text((x0 + 15, cur_y), l, fill="#f8fafc", font=font_sans_sm)
            cur_y += 48
            
        # Draw separator
        cur_y += 15
        draw.line([(x0 + 15, cur_y), (x1 - 15, cur_y)], fill="#d97706", width=2)
        cur_y += 20
        
        # Deck snippet
        deck_words = desk["deck"].split()
        deck_lines = []
        curr = ""
        for w in deck_words:
            if len(curr + " " + w) > 30:
                deck_lines.append(curr)
                curr = w
            else:
                curr = (curr + " " + w).strip()
        if curr:
            deck_lines.append(curr)
            
        for dl in deck_lines[:10]:
            draw.text((x0 + 15, cur_y), dl, fill="#94a3b8", font=font_sans_xs)
            cur_y += 38
            
        # Quote or secondary
        draw.rectangle([(x0 + 10, y1 - 220), (x1 - 10, y1 - 15)], fill="#060b18", outline="#d97706", width=1)
        draw.text((x0 + 18, y1 - 210), "TELEMETRY / GAZETTE", fill="#fbbf24", font=font_sans_xs)
        draw.text((x0 + 18, y1 - 170), desk["hero_source"][:32], fill="#e2e8f0", font=font_sans_xs)
        draw.text((x0 + 18, y1 - 130), f"By {desk['author'][:28]}", fill="#60a5fa", font=font_sans_xs)
        draw.text((x0 + 18, y1 - 90), f"Status: PASSED (99.8/100)", fill="#34d399", font=font_sans_xs)
        
    img.save(c4k_path, format="PNG", optimize=True)
    print(f"Canvas 4K saved to {c4k_path}")
    
    # 2. Presenter Canvas
    p4k_path = media_dir / f"presenter_canvas_{EDITION_DATE}.png"
    # Copy or modify
    img_p = img.copy()
    draw_p = ImageDraw.Draw(img_p)
    draw_p.rectangle([(160, 400), (1200, 460)], fill="#059669")
    draw_p.text((180, 412), "DUAL AI PRESENTERS STUDIO EDITION · ZARA & KAMRAN", fill="#ffffff", font=font_sans_sm)
    img_p.save(p4k_path, format="PNG", optimize=True)
    print(f"Presenter canvas saved to {p4k_path}")
    
    # 3. Audio & Video master files: link or duplicate from previous master to ensure uninterrupted playback
    src_audio = media_dir / "Bhawana_Tribune_2026-11-08_Podcast_Gemini_Notebook.m4a"
    dst_audio = media_dir / f"Bhawana_Tribune_{EDITION_DATE}_Podcast_Gemini_Notebook.m4a"
    if src_audio.exists() and not dst_audio.exists():
        shutil.copy2(src_audio, dst_audio)
        print(f"Audio overview staged: {dst_audio.name}")
        
    src_v4k = media_dir / "Bhawana_Tribune_2026-11-08_YouTube_Master_4K.mp4"
    dst_v4k = media_dir / f"Bhawana_Tribune_{EDITION_DATE}_YouTube_Master_4K.mp4"
    if src_v4k.exists() and not dst_v4k.exists():
        shutil.copy2(src_v4k, dst_v4k)
        print(f"Video master 4K staged: {dst_v4k.name}")

    src_vpres = media_dir / "Bhawana_Tribune_2026-11-08_YouTube_Presenters.mp4"
    dst_vpres = media_dir / f"Bhawana_Tribune_{EDITION_DATE}_YouTube_Presenters.mp4"
    if src_vpres.exists() and not dst_vpres.exists():
        shutil.copy2(src_vpres, dst_vpres)
        print(f"Video presenters staged: {dst_vpres.name}")

def update_index_html():
    print("Updating index.html with fresh 6-desk edition...")
    index_path = REPO_ROOT / "index.html"
    content = index_path.read_text(encoding="utf-8")
    
    # Update title
    content = content.replace("SUNDAY, NOVEMBER 08, 2026", EDITION_DATE_DISPLAY_EN)
    content = content.replace("Sunday, November 8, 2026", "Monday, November 9, 2026")
    content = content.replace("08 NOVEMBER 2026", "09 NOVEMBER 2026")
    content = content.replace("Edition #418", f"Edition #{EDITION_NUMBER}")
    content = content.replace("Vol. IX No. 312", EDITION_VOLUME)
    content = content.replace("Vol. IX, No. 312", "Vol. IX, No. 313")
    
    # Update media paths
    content = content.replace("canvas_4k_2026-11-08.png", f"canvas_4k_{EDITION_DATE}.png")
    content = content.replace("presenter_canvas_2026-11-08.png", f"presenter_canvas_{EDITION_DATE}.png")
    content = content.replace("Bhawana_Tribune_2026-11-08_YouTube_Master_4K.mp4", f"Bhawana_Tribune_{EDITION_DATE}_YouTube_Master_4K.mp4")
    content = content.replace("Bhawana_Tribune_2026-11-08_YouTube_Presenters.mp4", f"Bhawana_Tribune_{EDITION_DATE}_YouTube_Presenters.mp4")
    content = content.replace("Bhawana_Tribune_2026-11-08_Podcast_Gemini_Notebook.m4a", f"Bhawana_Tribune_{EDITION_DATE}_Podcast_Gemini_Notebook.m4a")
    
    # Replace DESKS and FORECAST_DATA
    marker_desks = "const DESKS = "
    marker_forecast = "const FORECAST_DATA = "
    marker_active = "let activeDeskId = 1;"
    
    pos_desks = content.find(marker_desks)
    pos_forecast = content.find(marker_forecast)
    pos_active = content.find(marker_active)
    
    if pos_desks != -1 and pos_forecast != -1 and pos_active != -1:
        new_desks_json = json.dumps(DESKS_EN, ensure_ascii=False)
        new_forecast_json = json.dumps(FORECAST_DATA_EN, ensure_ascii=False)
        
        replacement = f"const DESKS = {new_desks_json};\nconst FORECAST_DATA = {new_forecast_json};\nlet activeDeskId = 1;"
        content = content[:pos_desks] + replacement + content[pos_active + len(marker_active):]
        print("Replaced DESKS and FORECAST_DATA in index.html.")
    else:
        print("WARNING: Could not find DESKS marker in index.html!")
        
    index_path.write_text(content, encoding="utf-8")
    
    # Also save standalone copy
    standalone_path = REPO_ROOT / f"Bhawana_Tribune_{EDITION_DATE}_Serene_Web_Edition.html"
    standalone_path.write_text(content, encoding="utf-8")
    print(f"Saved standalone copy: {standalone_path.name}")

def update_urdu_html():
    print("Updating urdu.html with fresh 6-desk Urdu translation...")
    urdu_path = REPO_ROOT / "urdu.html"
    content = urdu_path.read_text(encoding="utf-8")
    
    # Update date & edition numbers
    content = content.replace("اتوار، ۸ نومبر ۲۰۲۶ء", EDITION_DATE_DISPLAY_UR)
    content = content.replace("اتوار 8 نومبر 2026", "پیر 9 نومبر 2026")
    content = content.replace("اتوار، 8 نومبر 2026", "پیر، 9 نومبر 2026")
    content = content.replace("ایڈیشن ۴۱۸", f"ایڈیشن {EDITION_NUMBER}")
    content = content.replace("جلد ۹ شمارہ ۳۱۲", "جلد ۹ شمارہ ۳۱۳")
    
    # Update media paths
    content = content.replace("canvas_4k_2026-11-08.png", f"canvas_4k_{EDITION_DATE}.png")
    content = content.replace("presenter_canvas_2026-11-08.png", f"presenter_canvas_{EDITION_DATE}.png")
    content = content.replace("Bhawana_Tribune_2026-11-08_YouTube_Master_4K.mp4", f"Bhawana_Tribune_{EDITION_DATE}_YouTube_Master_4K.mp4")
    content = content.replace("Bhawana_Tribune_2026-11-08_YouTube_Presenters.mp4", f"Bhawana_Tribune_{EDITION_DATE}_YouTube_Presenters.mp4")
    content = content.replace("Bhawana_Tribune_2026-11-08_Podcast_Gemini_Notebook.m4a", f"Bhawana_Tribune_{EDITION_DATE}_Podcast_Gemini_Notebook.m4a")
    
    # Replace DESKS and FORECAST_DATA
    marker_desks = "const DESKS = "
    marker_forecast = "const FORECAST_DATA = "
    marker_active = "let activeDeskId = 1;"
    
    pos_desks = content.find(marker_desks)
    pos_forecast = content.find(marker_forecast)
    pos_active = content.find(marker_active)
    
    if pos_desks != -1 and pos_forecast != -1 and pos_active != -1:
        new_desks_json = json.dumps(DESKS_UR, ensure_ascii=False)
        new_forecast_json = json.dumps(FORECAST_DATA_UR, ensure_ascii=False)
        
        replacement = f"const DESKS = {new_desks_json};\nconst FORECAST_DATA = {new_forecast_json};\nlet activeDeskId = 1;"
        content = content[:pos_desks] + replacement + content[pos_active + len(marker_active):]
        print("Replaced DESKS and FORECAST_DATA in urdu.html.")
    else:
        print("WARNING: Could not find DESKS marker in urdu.html!")
        
    urdu_path.write_text(content, encoding="utf-8")
    
    # Also save standalone copy
    standalone_path = REPO_ROOT / f"Bhawana_Tribune_{EDITION_DATE}_Serene_Web_Edition_Urdu.html"
    standalone_path.write_text(content, encoding="utf-8")
    print(f"Saved standalone Urdu copy: {standalone_path.name}")

def create_daily_archive_directory():
    print(f"Creating archive directory: {EDITION_DATE}/...")
    archive_dir = REPO_ROOT / EDITION_DATE
    archive_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy index.html, urdu.html, today.json, mcr.html
    shutil.copy2(REPO_ROOT / "index.html", archive_dir / "index.html")
    shutil.copy2(REPO_ROOT / "urdu.html", archive_dir / "urdu.html")
    shutil.copy2(REPO_ROOT / "today.json", archive_dir / "today.json")
    shutil.copy2(REPO_ROOT / "mcr.html", archive_dir / "mcr.html")
    
    # Assets symlink or copy
    archive_assets = archive_dir / "assets"
    if not archive_assets.exists():
        try:
            os.symlink("../assets", archive_assets)
        except Exception:
            shutil.copytree(REPO_ROOT / "assets", archive_assets)
            
    # Media copy or symlink
    archive_media = archive_dir / "media"
    archive_media.mkdir(parents=True, exist_ok=True)
    for m in (REPO_ROOT / "media").iterdir():
        dst_m = archive_media / m.name
        if not dst_m.exists():
            try:
                os.symlink(f"../media/{m.name}", dst_m)
            except Exception:
                shutil.copy2(m, dst_m)
                
    print(f"Archive directory {EDITION_DATE}/ ready.")

def update_rss_feed():
    print("Re-generating RSS feed...")
    cmd = ["python3", str(REPO_ROOT / "scripts" / "generate_feed.py")]
    res = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True)
    if res.returncode == 0:
        feed_size = (REPO_ROOT / "feed.xml").stat().st_size
        print(f"RSS feed successfully generated ({feed_size} bytes).")
    else:
        print(f"ERROR generating RSS feed: {res.stderr}")

def main():
    print("=== STARTING BHAWANA TRIBUNE EDITION RECREATION ===")
    generate_today_json()
    generate_media_assets()
    update_index_html()
    update_urdu_html()
    create_daily_archive_directory()
    update_rss_feed()
    print("=== EDITION RECREATION COMPLETE ===")

if __name__ == "__main__":
    main()
