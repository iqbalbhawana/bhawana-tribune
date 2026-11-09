#!/usr/bin/env python3
"""
Bhawana Tribune — Page 3 Editorial Update Engine
Applies founder & editor-in-chief's FT/NYT conversational editorial standard:
- 'EDITORIAL' clearly mentioned at top
- Natural progression of 2-3 commentaries on news of the day across 4 paragraphs
- Taxation, economic, and financial commentary:
  1. Customs EPZ Risalpur Shippo Pvt Ltd stock shortage audit
  2. FBR disallowing wash sales, cross trades & tax swaps for TY 2027
  3. NEPRA Rs2.37/unit tariff increase on package beneficiaries
  4. Synthesis: Tax benefit and tax burden travel together, verified by reconciliation
"""

import json
import re
from pathlib import Path

REPO_ROOT = Path("/home/antigravity/bhawana-tribune")

EDITORIAL_EN = {
    "title": "Audit, Assessment and the Arithmetic of Revenue",
    "deck": "Customs moves against an EPZ unit at Risalpur, the FBR closes the wash-sale window for 2027, and NEPRA's Rs2.37 lands only on package beneficiaries — Page 3 reads the statutory spine of yesterday's headlines.",
    "paragraphs": [
        "Page 1 yesterday carried the news that Pakistan Customs has initiated legal proceedings against M/s Shippo Private Limited, an industrial unit operating in the Export Processing Zone at Risalpur, after the Collectorate of Customs detected alleged import irregularities and a substantial shortage of goods during audit and stock-taking proceedings. Read as a statutory matter, the development is unremarkable in form and significant in substance. EPZ concessions are conditional privileges: imports enter on the explicit statutory understanding that they will be accounted for in production and export. When stock-taking reveals a shortage between what the record shows and what the premises hold, the customs assessment regime must respond, because every unaccounted unit is a unit that travelled duty-free without discharging its statutory condition. Revenue protection here is not harassment; it is the condition on which the concession stands.",
        "The second lead comes from the FBR, which has disallowed capital loss adjustment in wash sales, cross trades and tax swaps for tax year 2027. These are, in substance, positions where a security is sold and repurchased — or swapped between hands — to crystallise a loss on paper without parting with economic exposure. The statutory response is correct in method: where the transaction does not change economic ownership, the loss is an accounting artefact, not an assessable reality. Two points deserve emphasis. First, the disallowance is framed prospectively for 2027, which gives traders a clean cut-off and spares earlier assessment years a retrospective fight. Second, it shifts the assessment conversation from documentation to substance — the question is no longer whether a loss was booked, but whether economic ownership genuinely changed.",
        "The fiscal lead of the day belongs to NEPRA, which has raised the electricity tariff by Rs2.37 per unit for November 2026 bills, with the Power Division clarifying that the increase applies only to package beneficiaries. Tariff determination is a statutory exercise, but its incidence is always distributive: the same Rs2.37 lands differently on a consumer inside a negotiated package than on one outside it. The clarification narrows the field of those who bear the adjustment, and it is a useful reminder that a regulatory headline cannot be read without its eligibility annexure. For bill-payers, the practical course is to test their own category against the announcement rather than against the number.",
        "What binds the three leads is a single statutory proposition: tax benefit and tax burden travel together, and each is verified by reconciliation. Customs reconciles imports against physical stock; the FBR reconciles booked losses against economic substance; tariff policy reconciles a uniform headline number against differentiated incidence. For those under audit — as the Risalpur unit now is — the defence is arithmetic done early: stock registers that match ledgers, imports that match production. For those trading toward 2027, the defence is structuring that survives a substance test. Statutory discipline is not a season; it is a standing condition of doing business where the revenue is a party to every transaction."
    ]
}

EDITORIAL_UR = {
    "title": "آڈٹ، اسسمنٹ اور ریونیو کی حسابی حقیقت",
    "deck": "رسالپور ای پی زیڈ یونٹ کے خلاف کسٹمز کارروائی، ایف بی آر کی جانب سے 2027 کے لیے واش سیلز پر پابندی، اور نیپرا کا 2.37 روپے فی یونٹ اضافہ صرف پیکیج صارفین کے لیے — صفحہ 3 کل کی خبروں کی قانونی روح اور حقیقت کا احاطہ کرتا ہے۔",
    "paragraphs": [
        "کل صفحہ 1 پر یہ خبر نمایاں تھی کہ پاکستان کسٹمز نے رسالپور کے ایکسپورٹ پروسیسنگ زون میں کام کرنے والے صنعتی یونٹ میسرز شپو پرائیویٹ لمیٹڈ کے خلاف قانونی کارروائی کا آغاز کر دیا ہے، جب کسٹمز کلکٹریٹ نے آڈٹ اور سٹاک چیکنگ کے دوران مبینہ درآمدی بے ضابطگیوں اور سامان کی نمایاں کمی کا انکشاف کیا۔ قانونی نقطہ نظر سے دیکھیں تو یہ پیش رفت اپنی ساخت میں عام لیکن اپنے اثرات میں انتہائی اہم ہے۔ ای پی زیڈ مراعات مشروط حقوق ہیں: خام مال اور سامان اس واضح قانونی یقین دہانی پر ڈیوٹی فری آتا ہے کہ اسے پیداوار اور برآمدات کے کھاتوں میں دکھایا جائے گا۔ جب سٹاک چیکنگ سے کاغذی ریکارڈ اور اصل گودام کے درمیان فرق سامنے آئے تو کسٹمز کے تشخیصی نظام کو حرکت میں آنا ہی ہوتا ہے، کیونکہ غائب ہونے والا ہر یونٹ دراصل وہ مال ہے جو قانونی شرط پوری کیے بغیر ٹیکس فری گزر گیا۔ یہاں محصولات کا تحفظ ہراساں کرنا نہیں بلکہ اس رعایت کی بنیادی بنیاد ہے۔",
        "دوسری بڑی پیش رفت فیڈرل بورڈ آف ریونیو (ایف بی آر) کی طرف سے سامنے آئی ہے، جس نے مالی سال 2027 کے لیے واش سیلز، کراس ٹریڈز اور ٹیکس سویپس میں کیپیٹل لاس ایڈجسٹمنٹ کو مسترد کر دیا ہے۔ یہ بنیادی طور پر وہ سودے ہیں جہاں سیکیورٹیز کو کاغذی نقصان دکھانے کے لیے بیچا اور فوراً واپس خریدا جاتا ہے، جبکہ اصل معاشی ملکیتی رسک تبدیل نہیں ہوتا۔ ایف بی آر کا قانونی ردعمل اپنے طریقہ کار میں بالکل درست ہے: جہاں لین دین سے معاشی ملکیت تبدیل نہ ہو، وہاں نقصان صرف کھاتے کی ایک کاغذی اختراع ہے، حقیقی قابلِ تشخیص خسارہ نہیں۔ یہاں دو نکات قابلِ غور ہیں۔ اول، یہ پابندی ٹیکس سال 2027 کے لیے آگے کے وقت سے نافذ کی گئی ہے، جس سے مارکیٹ ٹریڈرز کو ایک واضح خط مل گیا ہے اور ماضی کے سالوں پر بلاوجہ تنازعہ کھڑا نہیں ہوا۔ دوم، یہ ٹیکس تشخیص کی بحث کو محض کاغذی کارروائی سے ہٹا کر معاشی حقیقت کی طرف لاتا ہے—اب سوال یہ نہیں کہ کھاتے میں نقصان درج ہے یا نہیں، بلکہ یہ ہے کہ کیا معاشی ملکیت واقعی تبدیل ہوئی ہے۔",
        "دن کی تیسری مالیاتی خبر نیپرا کی ہے، جس نے نومبر 2026 کے بجلی کے بلوں میں 2.37 روپے فی یونٹ اضافہ کیا ہے، البتہ وزارتِ توانائی نے واضح کیا کہ اس اضافے کا اطلاق صرف رعایتی پیکیج کے حامل صارفین پر ہوگا۔ بجلی کے نرخوں کا تعین اگرچہ ایک قانونی عمل ہے، لیکن اس کا بوجھ ہمیشہ طبقاتی تقسیم کے تحت ہوتا ہے: وہی 2.37 روپے رعایتی پیکیج کے اندر موجود صارف پر مختلف انداز سے پڑتے ہیں اور عام صارف پر الگ۔ وزارت کی وضاحت نے ان صارفین کے دائرے کو محدود کر دیا ہے جو یہ بوجھ اٹھائیں گے، اور یہ اس بات کی اہم یاد دہانی ہے کہ کسی ریگولیٹری ہیڈلائن کو اس کی اہلیت کے ضمیمے کے بغیر نہیں پڑھا جا سکتا۔ بل ادا کرنے والوں کے لیے عملی طریقہ یہ ہے کہ وہ صرف مجموعی اعداد و شمار دیکھنے کے بجائے اپنے مخصوص ٹیرف کیٹیگری کو پرکھیں۔",
        "ان تینوں خبروں کو جوڑنے والی ایک ہی مشترکہ قانونی حقیقت ہے: ٹیکس کی مراعات اور ٹیکس کا بوجھ ہمیشہ ساتھ ساتھ چلتے ہیں، اور دونوں کا دارومدار کھاتوں کے حسابی ملاپ (Reconciliation) پر ہے۔ کسٹمز درآمدات کو جسمانی سٹاک سے ملاتا ہے؛ ایف بی آر کاغذی نقصانات کو اصل معاشی حقیقت سے پرکھتا ہے؛ اور ٹیرف پالیسی یکساں ریگولیٹری اعداد کو نچلی سطح کے صارفین کے مطابق تقسیم کرتی ہے۔ ان کاروباری اداروں کے لیے جو آڈٹ کی زد میں ہیں—جیسا کہ رسالپور کا صنعتی یونٹ—سب سے مضبوط دفاع بروقت حسابی شفافیت ہے: وہ سٹاک رجسٹر جو کھاتوں کے بالکل مطابق ہوں اور وہ درآمدات جو حقیقی پیداوار سے میل کھاتی ہوں۔ اور 2027 کی مارکیٹ کی طرف دیکھنے والوں کے لیے دفاع ایسا سٹرکچر ہے جو کاغذی کے بجائے حقیقی معاشی امتحان پر پورا اترے۔ قانونی و ٹیکس نظم و ضبط محض کسی ایک سیزن کا نام نہیں؛ یہ کاروبار چلانے کی مستقل شرط ہے جہاں قومی خزانہ ہر کاروباری لین دین کا فریق ہے۔"
    ]
}

def update_build_script():
    build_path = REPO_ROOT / "scripts" / "build_edition_2026_11_09.py"
    content = build_path.read_text(encoding="utf-8")
    
    # 1. Update English editorial object in build script
    old_en_marker = '"title": "The Sovereign Quality Gate: Machine Cognition and the Imperative of Local Verification",'
    if old_en_marker in content:
        # Replace the entire editorial dictionary for EN
        pattern_en = r'"editorial":\s*\{\s*"title":\s*"The Sovereign Quality Gate:[^}]+\]\s*\}'
        new_en_json = '"editorial": ' + json.dumps(EDITORIAL_EN, ensure_ascii=False, indent=12)
        content = re.sub(pattern_en, new_en_json, content, flags=re.DOTALL)
        print("Updated English editorial in build script.")
    
    # Update quote for Desk 3 EN
    old_quote_en = "Deterministic local quality gates are the non-negotiable safeguard that transforms artificial cognition into trusted sovereign infrastructure. — Muhammad Iqbal Bhawana"
    new_quote_en = "Statutory discipline is not a season; it is a standing condition of doing business where the revenue is a party to every transaction. — Lead Broadsheet Editorial, Bhawana Tribune"
    content = content.replace(old_quote_en, new_quote_en)
    
    # 2. Update Urdu editorial object in build script
    old_ur_marker = '"title": "خودمختار کوالٹی گیٹ: مشینی ذہانت اور مقامی تصدیق کا ناگزیر تقاضا",'
    if old_ur_marker in content:
        pattern_ur = r'"editorial":\s*\{\s*"title":\s*"خودمختار کوالٹی گیٹ:[^}]+\]\s*\}'
        new_ur_json = '"editorial": ' + json.dumps(EDITORIAL_UR, ensure_ascii=False, indent=12)
        content = re.sub(pattern_ur, new_ur_json, content, flags=re.DOTALL)
        print("Updated Urdu editorial in build script.")

    old_quote_ur = "مصنوعی ذہانت کو خودمختار عوامی انفراسٹرکچر بنانے کے لیے مقامی سطح پر معیار کی فول پروف جانچ ناگزیر ہے۔ — محمد اقبال بھوانہ"
    new_quote_ur = "قانونی و ٹیکس نظم و ضبط محض کسی ایک سیزن کا نام نہیں؛ یہ کاروبار چلانے کی مستقل شرط ہے جہاں قومی خزانہ ہر کاروباری لین دین کا فریق ہے۔ — اداریہ، بھوانہ ٹریبیون"
    content = content.replace(old_quote_ur, new_quote_ur)

    build_path.write_text(content, encoding="utf-8")
    print("build_edition_2026_11_09.py successfully updated.")

def update_html_templates():
    # Update index.html and standalone to add the EDITORIAL badge
    badge_en = '<div class="editorial-badge" style="display: inline-block; font-family: monospace; font-size: 11px; font-weight: 800; letter-spacing: 2px; text-transform: uppercase; color: #f59e0b; background: rgba(245, 158, 11, 0.12); border: 1px solid rgba(245, 158, 11, 0.4); padding: 5px 14px; border-radius: 6px; margin-bottom: 14px;">EDITORIAL</div>'
    badge_ur = '<div class="editorial-badge" style="display: inline-block; font-size: 13px; font-weight: 800; color: #f59e0b; background: rgba(245, 158, 11, 0.15); border: 1px solid rgba(245, 158, 11, 0.4); padding: 5px 16px; border-radius: 6px; margin-bottom: 14px; font-family: sans-serif; letter-spacing: 1px;">اداریہ • EDITORIAL</div>'

    for p in [REPO_ROOT / "index.html", REPO_ROOT / "Bhawana_Tribune_2026-11-09_Serene_Web_Edition.html", REPO_ROOT / "2026-11-09" / "index.html"]:
        if p.exists():
            txt = p.read_text(encoding="utf-8")
            if '<div class="editorial-badge"' not in txt:
                txt = txt.replace(
                    '<div class="editorial-special">\n        <div class="editorial-special-title">',
                    f'<div class="editorial-special">\n        {badge_en}\n        <div class="editorial-special-title">'
                )
                p.write_text(txt, encoding="utf-8")
                print(f"Added EDITORIAL badge to {p.name}")

    for p in [REPO_ROOT / "urdu.html", REPO_ROOT / "Bhawana_Tribune_2026-11-09_Serene_Web_Edition_Urdu.html", REPO_ROOT / "2026-11-09" / "urdu.html"]:
        if p.exists():
            txt = p.read_text(encoding="utf-8")
            if '<div class="editorial-badge"' not in txt:
                txt = txt.replace(
                    '<div class="editorial-special">\n        <div class="editorial-special-title">',
                    f'<div class="editorial-special">\n        {badge_ur}\n        <div class="editorial-special-title">'
                )
                p.write_text(txt, encoding="utf-8")
                print(f"Added EDITORIAL badge to {p.name}")

def update_today_json():
    today_paths = [REPO_ROOT / "today.json", REPO_ROOT / "2026-11-09" / "today.json"]
    for p in today_paths:
        if p.exists():
            d = json.loads(p.read_text(encoding="utf-8"))
            for art in d.get("articles", []):
                if art["id"] == 3:
                    art["editorial"] = EDITORIAL_EN
                    art["quote"] = "Statutory discipline is not a season; it is a standing condition of doing business where the revenue is a party to every transaction. — Lead Broadsheet Editorial, Bhawana Tribune"
            p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"Updated {p.name} with new editorial.")

if __name__ == "__main__":
    update_build_script()
    update_html_templates()
    update_today_json()
    print("Page 3 Editorial updates applied successfully.")
