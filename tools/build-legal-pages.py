#!/usr/bin/env python3
"""Generate terms/index.html and privacy/index.html (run from repo root)."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LEGAL_EXTRA_CSS = """
.legal-nav .lang-switch { margin-inline-start: auto; }
@media (min-width: 900px) {
  .legal-nav .nav__links { margin-inline-start: 0.5rem; }
}
.legal-doc { max-width: 44rem; margin: 0 auto; padding: 2.25rem var(--gutter) 3.5rem; }
.legal-doc h1 { margin: 0 0 1rem; font-size: clamp(1.85rem, 5vw, 2.35rem); font-weight: 700; letter-spacing: -0.02em; line-height: 1.15; }
.legal-doc h2 { margin: 2rem 0 0.65rem; font-size: 1.15rem; font-weight: 700; color: var(--text); }
.legal-doc p { margin: 0.65rem 0; color: var(--text); }
.legal-doc ul { margin: 0.5rem 0 0.65rem; padding-inline-start: 1.35rem; color: var(--text); }
.legal-doc li { margin: 0.35rem 0; }
.legal-doc a { color: var(--gold); }
.legal-doc .legal-updated { margin-top: 2rem; font-size: 0.9rem; color: var(--muted); }
"""

FOOTER = """
  <footer class="footer">
    <p class="footer__nav"><a href="https://elghaly.dev/">elghaly.dev</a> · <a href="/">Chatting</a> · <a href="https://elghaly.dev/plumb">Plumb</a> · <a href="https://elghaly.dev/quay">QUAY</a> · <a href="https://elghaly.dev/about.html">About</a> · <a href="https://elghaly.dev/contact.html">Contact</a> · <a href="https://elghaly.dev/refund.html">Refunds</a> · <a href="https://elghaly.dev/delivery.html">Delivery</a> · <a href="/terms/">Terms</a> · <a href="/privacy/">Privacy</a></p>
    <p>elghaly · Email first: <a href="mailto:support@elghaly.dev">support@elghaly.dev</a>. Calls only by appointment.</p>
    <p class="lic-badges"><a href="https://creativecommons.org/licenses/by/4.0/" rel="license">© elghaly · CC BY 4.0</a> <a href="https://github.com/Alarm2024/elghaly/blob/main/LICENSE">Code: MIT</a> <a href="https://github.com/Alarm2024">Open source</a></p>
  </footer>
"""

HEADER = """
  <a class="skip" href="#main">Skip to content</a>
  <header class="nav">
    <div class="nav__in legal-nav">
      <a class="brand" href="https://elghaly.dev/" aria-label="elghaly home">elghaly</a>
      <div class="lang-switch" role="group" aria-label="Language">
        <button type="button" class="lang-btn" data-lang="en">EN</button>
        <button type="button" class="lang-btn" data-lang="ar">AR</button>
        <button type="button" class="lang-btn" data-lang="ru">RU</button>
        <button type="button" class="lang-btn" data-lang="zh">ZH</button>
      </div>
      <nav class="nav__links nav__links--always" aria-label="Main">
        <a href="/">Chatting</a>
        <a href="https://elghaly.dev/plumb">Plumb</a>
        <a href="https://elghaly.dev/quay">QUAY</a>
        <a href="https://elghaly.dev/contact.html">Contact</a>
      </nav>
    </div>
  </header>
"""


def shell(page: str, title: str, canonical: str, description: str, body_panels: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <meta name="description" content="{description}">
  <meta name="theme-color" content="#352373">
  <title>{title}</title>
  <link rel="canonical" href="{canonical}">
  <link rel="icon" href="/favicon.ico?v=e1" sizes="any">
  <link rel="icon" href="/favicon.svg?v=e1" type="image/svg+xml">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png?v=e1">
  <link rel="manifest" href="/site.webmanifest?v=e1">
  <link rel="stylesheet" href="/assets/chatting-glass.css">
  <style>{LEGAL_EXTRA_CSS}</style>
</head>
<body>
{HEADER}
  <main id="main" class="legal-doc">
{body_panels}
  </main>
{FOOTER}
  <script src="/assets/legal.js" defer></script>
</body>
</html>
"""


TERMS = {
    "en": {
        "title": "Terms of Service — Chatting · elghaly",
        "h1": "Terms of Service",
        "updated": "Last updated: October 2026",
        "blocks": """
    <p>These terms apply to Chatting, a paid service from elghaly at <a href="/">chatting.elghaly.dev</a>.</p>
    <h2>The service</h2>
    <p>Chatting offers private, one-to-one online sessions. We help you choose, set up and train an AI assistant on <strong>your own accounts</strong>, with <strong>you at the keyboard</strong>. We guide; you stay in control of every login and click.</p>
    <h2>Courses</h2>
    <ul>
      <li><strong>Starter:</strong> three 1:1 sessions within 35 days — safety basics, choosing an assistant, and first daily tasks.</li>
      <li><strong>Full:</strong> ten 1:1 sessions within 35 days — everything in Starter, plus deeper training, permissions, tool connections, and daily routines.</li>
      <li><strong>Flexible:</strong> 1:1 sessions when you need them, inside 35 days or beyond, on the topics you pick each time.</li>
    </ul>
    <p>Every session is private and priced per client. You receive a fixed price by email before anything is booked.</p>
    <h2>Booking and rescheduling</h2>
    <p>Request a quote, confirm a course, and schedule or reschedule sessions by email. Nothing is booked until you agree to the price and times we propose.</p>
    <h2>What we never ask for</h2>
    <p>We never ask for or accept your passwords, keys, seed phrases, or card details — not by email, not on a call, not in a session. If anyone asks in our name, it is not us.</p>
    <h2>Your results</h2>
    <p>Outcomes depend on how you use your own tools and accounts after our sessions. We teach and set up with you; we make no promise of specific results. Check your assistant’s work before you rely on it.</p>
    <h2>Refunds</h2>
    <p>If a session was not useful, ask and you get your money back: no form and no time limit. Email <a href="mailto:support@elghaly.dev">support@elghaly.dev</a>. See the <a href="https://elghaly.dev/refund.html">refund policy</a> and our <a href="/privacy/">privacy policy</a>.</p>
    <h2>Contact</h2>
    <p>Email first: <a href="mailto:support@elghaly.dev">support@elghaly.dev</a>. Calls only by appointment.</p>
    <p>elghaly, LLC</p>
""",
    },
    "ar": {
        "title": "شروط الخدمة — Chatting · elghaly",
        "h1": "شروط الخدمة",
        "updated": "آخر تحديث: أكتوبر 2026",
        "blocks": """
    <p>تنطبق هذه الشروط على Chatting، خدمة مدفوعة من elghaly على <a href="/">chatting.elghaly.dev</a>.</p>
    <h2>الخدمة</h2>
    <p>يقدّم Chatting جلسات خاصة فردية عبر الإنترنت. نساعدك على اختيار مساعد ذكاء اصطناعي وإعداده وتدريبه على <strong>حساباتك أنت</strong>، و<strong>أنت على لوحة المفاتيح</strong>. نحن نرشد؛ وأنت تبقى مسيطراً على كل تسجيل دخول وكل نقرة.</p>
    <h2>المسارات</h2>
    <ul>
      <li><strong>Starter:</strong> ثلاث جلسات فردية خلال 35 يوماً — أساسيات الأمان، اختيار المساعد، وأول مهام يومية.</li>
      <li><strong>Full:</strong> عشر جلسات فردية خلال 35 يوماً — كل ما في Starter، مع تدريب أعمق وصلاحيات وربط أدوات وروتين يومي.</li>
      <li><strong>Flexible:</strong> جلسات فردية عند الحاجة، خلال 35 يوماً أو بعدها، حسب الموضوع الذي تختاره في كل مرة.</li>
    </ul>
    <p>كل جلسة خاصة والتسعير لكل عميل. تصلك سعر ثابت بالبريد قبل أي حجز.</p>
    <h2>الحجز وإعادة الجدولة</h2>
    <p>اطلب عرض سعر، أكّد المسار، وجدول أو أعد جدولة الجلسات بالبريد. لا يُحجز شيء حتى توافق على السعر والأوقات التي نقترحها.</p>
    <h2>ما لا نطلبه أبداً</h2>
    <p>لا نطلب ولا نقبل كلمات المرور أو المفاتيح أو عبارات الاسترداد أو تفاصيل البطاقة — لا بالبريد ولا في مكالمة ولا في جلسة. إن طلب أحد ذلك باسمنا، فليس منا.</p>
    <h2>نتائجك</h2>
    <p>النتائج تعتمد على كيفية استخدامك لأدواتك وحساباتك بعد جلساتنا. نعلّم ونُعدّ معك؛ ولا نعد بنتائج محددة. راجع عمل مساعدك قبل أن تعتمد عليه.</p>
    <h2>استرداد المبالغ</h2>
    <p>If a session was not useful, ask and you get your money back: no form and no time limit. راسل <a href="mailto:support@elghaly.dev">support@elghaly.dev</a>. راجع <a href="https://elghaly.dev/refund.html">سياسة الاسترداد</a> و<a href="/privacy/">سياسة الخصوصية</a>.</p>
    <h2>التواصل</h2>
    <p>Email first: <a href="mailto:support@elghaly.dev">support@elghaly.dev</a>. Calls only by appointment.</p>
    <p>elghaly, LLC</p>
""",
    },
    "ru": {
        "title": "Условия — Chatting · elghaly",
        "h1": "Условия обслуживания",
        "updated": "Обновлено: октябрь 2026",
        "blocks": """
    <p>Эти условия относятся к Chatting — платной услуге elghaly на <a href="/">chatting.elghaly.dev</a>.</p>
    <h2>Услуга</h2>
    <p>Chatting — это частные онлайн-сессии один на один. Мы помогаем выбрать, настроить и обучить AI-ассистента на <strong>ваших собственных аккаунтах</strong>, пока <strong>вы сами нажимаете клавиши</strong>. Мы направляем; вы контролируете каждый вход и каждое действие.</p>
    <h2>Курсы</h2>
    <ul>
      <li><strong>Starter:</strong> три сессии 1:1 в течение 35 дней — безопасность, выбор ассистента, первые ежедневные задачи.</li>
      <li><strong>Full:</strong> десять сессий 1:1 в течение 35 дней — всё из Starter плюс углублённое обучение, разрешения, подключение инструментов и рутины.</li>
      <li><strong>Flexible:</strong> сессии 1:1 по мере необходимости, в течение 35 дней или позже, с темами по вашему выбору.</li>
    </ul>
    <p>Каждая сессия частная; цена фиксируется для каждого клиента. Вы получаете её по email до бронирования.</p>
    <h2>Бронирование и перенос</h2>
    <p>Запросите расчёт, подтвердите курс и назначайте или переносите сессии по email. Ничего не бронируется, пока вы не согласны с ценой и временем.</p>
    <h2>Чего мы никогда не просим</h2>
    <p>Мы никогда не просим и не принимаем пароли, ключи, seed-фразы или данные карты — ни по email, ни на звонке, ни на сессии. Если кто-то просит от нашего имени — это не мы.</p>
    <h2>Ваши результаты</h2>
    <p>Итог зависит от того, как вы сами используете инструменты и аккаунты после сессий. Мы обучаем и настраиваем вместе с вами; мы не обещаем конкретных результатов. Проверяйте работу ассистента, прежде чем на неё опираться.</p>
    <h2>Возвраты</h2>
    <p>If a session was not useful, ask and you get your money back: no form and no time limit. Напишите на <a href="mailto:support@elghaly.dev">support@elghaly.dev</a>. См. <a href="https://elghaly.dev/refund.html">политику возврата</a> и <a href="/privacy/">политику конфиденциальности</a>.</p>
    <h2>Контакт</h2>
    <p>Email first: <a href="mailto:support@elghaly.dev">support@elghaly.dev</a>. Calls only by appointment.</p>
    <p>elghaly, LLC</p>
""",
    },
    "zh": {
        "title": "服务条款 — Chatting · elghaly",
        "h1": "服务条款",
        "updated": "更新：2026 年 10 月",
        "blocks": """
    <p>本条款适用于 elghaly 在 <a href="/">chatting.elghaly.dev</a> 提供的付费服务 Chatting。</p>
    <h2>服务说明</h2>
    <p>Chatting 提供私密的一对一在线课程。我们在<strong>您自己的账户</strong>上帮您选择、设置并训练 AI 助手，且<strong>由您亲自操作键盘</strong>。我们指导；您掌控每一次登录与点击。</p>
    <h2>课程</h2>
    <ul>
      <li><strong>Starter：</strong>35 天内三次 1:1 课程——安全基础、选择助手、首批日常任务。</li>
      <li><strong>Full：</strong>35 天内十次 1:1 课程——含 Starter 全部内容，并深入训练、权限、工具连接与日常流程。</li>
      <li><strong>Flexible：</strong>按需在 35 天内或之后预约 1:1 课程，每次主题由您选择。</li>
    </ul>
    <p>每次课程均为私密服务，按客户单独报价。预订前我们会通过邮件给出固定价格。</p>
    <h2>预约与改期</h2>
    <p>通过邮件请求报价、确认课程并安排或改期。在您同意我们提出的价格与时间之前，不会完成预订。</p>
    <h2>我们从不索取的内容</h2>
    <p>我们从不索取或接收您的密码、密钥、助记词或银行卡信息——无论邮件、通话或课程中皆然。若有人冒用我们的名义索取，那不是我们。</p>
    <h2>您的结果</h2>
    <p>成效取决于您在课程后如何使用自己的工具与账户。我们与您一起教学与设置；不对具体结果作出承诺。依赖助手之前请先核对它的输出。</p>
    <h2>退款</h2>
    <p>If a session was not useful, ask and you get your money back: no form and no time limit. 请发邮件至 <a href="mailto:support@elghaly.dev">support@elghaly.dev</a>。另见 <a href="https://elghaly.dev/refund.html">退款政策</a>与<a href="/privacy/">隐私政策</a>。</p>
    <h2>联系</h2>
    <p>Email first: <a href="mailto:support@elghaly.dev">support@elghaly.dev</a>. Calls only by appointment.</p>
    <p>elghaly, LLC</p>
""",
    },
}

PRIVACY = {
    "en": {
        "title": "Privacy Policy — Chatting · elghaly",
        "h1": "Privacy Policy",
        "updated": "Last updated: October 2026",
        "blocks": """
    <p>This policy describes Chatting at <a href="/">chatting.elghaly.dev</a>.</p>
    <p>We deeply respect your privacy rights under the CCPA/CPRA. We collect the minimum (just your email and what kind of work you do), never sell or share your personal information, and you can ask us to delete it anytime at <a href="mailto:support@elghaly.dev">support@elghaly.dev</a>.</p>
    <h2>What we collect</h2>
    <p>Your email address and a short description of the kind of work you do when you request a quote or book sessions. We do not ask for your name, company name, passwords, keys, or payment details by email.</p>
    <h2>Why we use it</h2>
    <p>To reply with a quote, schedule sessions, and support you during your course. We use it only for Chatting and related email from elghaly.</p>
    <h2>How long we keep it</h2>
    <p>We keep your information only as long as needed for those purposes. You can ask us to delete it at any time; we will remove it when you ask.</p>
    <h2>No selling or sharing</h2>
    <p>We do not sell your personal information. We do not share it with advertisers or data brokers.</p>
    <h2>Cookies and analytics on this site</h2>
    <p>The Chatting site (including this page and <a href="/">the home page</a>) loads no third-party analytics, advertising pixels, or tracking scripts. We serve fonts from our own domain. We do not set marketing cookies on these pages.</p>
    <h2>Deletion requests</h2>
    <p>Email <a href="mailto:support@elghaly.dev">support@elghaly.dev</a> from the address you used with us and ask us to delete your information. We will confirm when it is done.</p>
    <h2>Children</h2>
    <p>Chatting is for adults who can enter into a paid service agreement. We do not knowingly collect information from children.</p>
    <h2>Changes</h2>
    <p>We may update this policy. The date at the bottom of the page shows when it last changed. Continued use of Chatting after an update means you accept the revised policy.</p>
    <p>elghaly, LLC</p>
""",
    },
    "ar": {
        "title": "سياسة الخصوصية — Chatting · elghaly",
        "h1": "سياسة الخصوصية",
        "updated": "آخر تحديث: أكتوبر 2026",
        "blocks": """
    <p>تصف هذه السياسة Chatting على <a href="/">chatting.elghaly.dev</a>.</p>
    <p>We deeply respect your privacy rights under the CCPA/CPRA. We collect the minimum (just your email and what kind of work you do), never sell or share your personal information, and you can ask us to delete it anytime at <a href="mailto:support@elghaly.dev">support@elghaly.dev</a>.</p>
    <h2>ما نجمع</h2>
    <p>عنوان بريدك ووصفاً قصيراً لنوع عملك عند طلب عرض أو حجز جلسات. لا نطلب اسمك أو اسم شركتك أو كلمات المرور أو المفاتيح أو تفاصيل الدفع بالبريد.</p>
    <h2>لماذا نستخدمه</h2>
    <p>للرد بعرض سعر وجدولة الجلسات ودعمك أثناء مسارك. نستخدمه فقط لـ Chatting وللبريد المرتبط من elghaly.</p>
    <h2>مدة الاحتفاظ</h2>
    <p>نحتفظ بمعلوماتك فقط طالما يلزم لهذه الأغراض. يمكنك طلب حذفها في أي وقت؛ ونزيلها عند طلبك.</p>
    <h2>لا بيع ولا مشاركة</h2>
    <p>لا نبيع معلوماتك الشخصية. لا نشاركها مع المعلنين أو وسطاء البيانات.</p>
    <h2>ملفات تعريف الارتباط والتحليلات على هذا الموقع</h2>
    <p>موقع Chatting (بما في ذلك هذه الصفحة و<a href="/">الصفحة الرئيسية</a>) لا يحمّل تحليلات طرف ثالث أو بكسلات إعلانية أو سكربتات تتبع. نقدّم الخطوط من نطاقنا. لا نضع cookies تسويقية على هذه الصفحات.</p>
    <h2>طلبات الحذف</h2>
    <p>راسل <a href="mailto:support@elghaly.dev">support@elghaly.dev</a> من العنوان الذي استخدمته معنا واطلب حذف معلوماتك. سنؤكد عند الانتهاء.</p>
    <h2>الأطفال</h2>
    <p>Chatting للبالغين القادرين على اتفاق خدمة مدفوعة. لا نجمع عن قصد معلومات من الأطفال.</p>
    <h2>التغييرات</h2>
    <p>قد نحدّث هذه السياسة. التاريخ في أسفل الصفحة يوضح آخر تعديل. استمرارك في Chatting بعد التحديث يعني قبول السياسة المُحدَّثة.</p>
    <p>elghaly, LLC</p>
""",
    },
    "ru": {
        "title": "Политика конфиденциальности — Chatting · elghaly",
        "h1": "Политика конфиденциальности",
        "updated": "Обновлено: октябрь 2026",
        "blocks": """
    <p>Эта политика описывает Chatting на <a href="/">chatting.elghaly.dev</a>.</p>
    <p>We deeply respect your privacy rights under the CCPA/CPRA. We collect the minimum (just your email and what kind of work you do), never sell or share your personal information, and you can ask us to delete it anytime at <a href="mailto:support@elghaly.dev">support@elghaly.dev</a>.</p>
    <h2>Что мы собираем</h2>
    <p>Ваш email и краткое описание вида работы при запросе расчёта или бронировании. Мы не просим по email имя, компанию, пароли, ключи или платёжные данные.</p>
    <h2>Зачем мы это используем</h2>
    <p>Чтобы ответить с ценой, назначить сессии и поддерживать вас во время курса. Только для Chatting и связанной переписки elghaly.</p>
    <h2>Как долго храним</h2>
    <p>Только столько, сколько нужно для этих целей. Вы можете попросить удалить данные в любой момент — мы удалим по запросу.</p>
    <h2>Без продажи и передачи</h2>
    <p>Мы не продаём персональные данные и не передаём их рекламодателям или брокерам данных.</p>
    <h2>Файлы cookie и аналитика на сайте</h2>
    <p>Сайт Chatting (включая эту страницу и <a href="/">главную</a>) не загружает стороннюю аналитику, рекламные пиксели или скрипты отслеживания. Шрифты отдаются с нашего домена. Маркетинговые cookie на этих страницах не ставятся.</p>
    <h2>Запросы на удаление</h2>
    <p>Напишите на <a href="mailto:support@elghaly.dev">support@elghaly.dev</a> с адреса, который вы использовали, и попросите удалить данные. Подтвердим выполнение.</p>
    <h2>Дети</h2>
    <p>Chatting предназначен для взрослых, способных заключить платный договор. Мы сознательно не собираем данные детей.</p>
    <h2>Изменения</h2>
    <p>Мы можем обновлять политику. Дата внизу страницы показывает последнее изменение. Продолжение использования Chatting после обновления означает принятие новой редакции.</p>
    <p>elghaly, LLC</p>
""",
    },
    "zh": {
        "title": "隐私政策 — Chatting · elghaly",
        "h1": "隐私政策",
        "updated": "更新：2026 年 10 月",
        "blocks": """
    <p>本政策说明 <a href="/">chatting.elghaly.dev</a> 上的 Chatting 服务。</p>
    <p>We deeply respect your privacy rights under the CCPA/CPRA. We collect the minimum (just your email and what kind of work you do), never sell or share your personal information, and you can ask us to delete it anytime at <a href="mailto:support@elghaly.dev">support@elghaly.dev</a>.</p>
    <h2>我们收集的内容</h2>
    <p>您在请求报价或预约时提供的邮箱，以及简短的工作类型说明。我们不会通过邮件索取姓名、公司名、密码、密钥或付款信息。</p>
    <h2>使用目的</h2>
    <p>用于回复报价、安排课程并在学习过程中为您提供支持。仅用于 Chatting 及 elghaly 相关邮件往来。</p>
    <h2>保留期限</h2>
    <p>仅在实现上述目的所需期间保留。您可随时要求删除；收到请求后我们会移除。</p>
    <h2>不出售、不共享</h2>
    <p>我们不出售个人信息，也不与广告商或数据经纪商共享。</p>
    <h2>本站的 Cookie 与分析</h2>
    <p>Chatting 网站（含本页与<a href="/">首页</a>）不加载第三方分析、广告像素或跟踪脚本。字体由本站域名提供。这些页面不设置营销 Cookie。</p>
    <h2>删除请求</h2>
    <p>请用您曾使用的邮箱致信 <a href="mailto:support@elghaly.dev">support@elghaly.dev</a> 要求删除信息。完成后我们会确认。</p>
    <h2>儿童</h2>
    <p>Chatting 面向能够订立付费服务协议的成年人。我们不会故意收集儿童信息。</p>
    <h2>变更</h2>
    <p>我们可能更新本政策。页底日期为最近修订时间。更新后继续使用 Chatting 即表示接受修订后的政策。</p>
    <p>elghaly, LLC</p>
""",
    },
}


def panels(data: dict) -> str:
    out = []
    for code in ("en", "ar", "ru", "zh"):
        block = data[code]
        hidden = "" if code == "en" else " hidden"
        out.append(
            f'    <div data-lang-panel="{code}"{hidden}>\n'
            f'      <h1>{block["h1"]}</h1>\n'
            f'{block["blocks"]}\n'
            f'      <p class="legal-updated">{block["updated"]}</p>\n'
            f"    </div>"
        )
    return "\n".join(out)


def write_terms():
    body = panels(TERMS)
    html = shell(
        "terms",
        "Terms of Service — Chatting · elghaly",
        "https://chatting.elghaly.dev/terms/",
        "Terms of Service for Chatting: private 1:1 AI assistant sessions by elghaly.",
        body,
    )
    path = ROOT / "terms" / "index.html"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")


def write_privacy():
    body = panels(PRIVACY)
    html = shell(
        "privacy",
        "Privacy Policy — Chatting · elghaly",
        "https://chatting.elghaly.dev/privacy/",
        "Privacy policy for Chatting at chatting.elghaly.dev.",
        body,
    )
    path = ROOT / "privacy" / "index.html"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")


if __name__ == "__main__":
    write_terms()
    write_privacy()
    print("Wrote terms/index.html and privacy/index.html")
