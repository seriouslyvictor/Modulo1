+-----------------------------------------------------------------------+
| **PYTHON WEB DEVELOPMENT**                                            |
|                                                                       |
| **Flask Course Plan**                                                 |
|                                                                       |
| *From First Route to Deployment*                                      |
+-----------------------------------------------------------------------+

12 Sessions · 6 Weeks · 36 Hours

3-hour blocks, twice a week

Mixed ages · Hands-on focus · VS Code + Terminal

Course Overview

This course takes students from zero web development experience to
deploying a fully functional Flask application. Students arrive with
approximately 40 hours of core Python and a brief HTML/CSS crash course.
Over 12 sessions, they will learn how Python and HTML/CSS connect
through Flask, building progressively more complex web applications.

Every session is designed with teenagers in mind: minimal lecture,
maximum hands-on coding. The format prioritizes learning by building
over learning by listening.

**Pedagogical Approach**

-   Each 3-hour session follows a consistent rhythm: demo, guided
    practice, free practice

-   Lecture and demos are capped at approximately 40 minutes, with
    mini-challenges embedded to maintain engagement

-   Students practice on self-contained exercises each session, building
    confidence incrementally

-   The course builds toward TCC (final project) readiness, where
    students will apply everything independently

**Session Map**

  ----------------------------------------------------------------------------
  **\#**   **Session Title**        **Key Topics**
  -------- ------------------------ ------------------------------------------
  1        Flask Foundations        First routes, dev server, request/response
                                    cycle

  2        Templates with Jinja2    render_template, variables, logic blocks

  3        Template Inheritance +   base.html, blocks, linking CSS/images
           Static Files             

  4        Forms & User Input (GET) HTML forms, query parameters, request.args

  5        Forms & User Input       POST method, request.form, basic
           (POST)                   validation

  6        Data Persistence         SQLite, Flask-SQLAlchemy, models, first
                                    queries

  7        Full CRUD: Create & Read Form to database to listing page

  8        Full CRUD: Update &      Edit forms, delete confirmation
           Delete                   

  9        User Feedback & Polish   Flash messages, redirect, PRG pattern

  10       Auth Part 1: Sessions &  Sessions, login/logout, route protection
           Login                    

  11       Auth Part 2: Password    werkzeug.security, data ownership
           Hashing                  

  12       Deployment               Render/Railway, env variables, going live
  ----------------------------------------------------------------------------

**Prerequisites**

-   Approximately 40 hours of core Python (variables, functions, loops,
    data structures, classes)

-   Basic HTML/CSS crash course completed (can write simple pages with
    tags, classes, selectors)

-   VS Code installed with Python extension, terminal comfort

-   Flask and pip already installed and working

+-----------------------------------------------------------------------+
| **SESSION 1**                                                         |
|                                                                       |
| **Flask Foundations**                                                 |
|                                                                       |
| *\"Hello, Web!\" --- From Python script to running website*           |
+-----------------------------------------------------------------------+

  ----------------------- -----------------------------------------------
  **Duration:** 3 hours   **Goal:** Students go from zero to a running
                          Flask app with multiple routes and understand
                          what happens when a browser visits a URL.

  ----------------------- -----------------------------------------------

**Time Breakdown**

  ---------- -------------------- ----------------------------------------
  **0:00 --  **Demo & Lecture**   Opening hook, first app,
  0:40**                          request/response, routes

  **0:40 --  **Mini-Challenge**   Quick check: write a route without
  0:45**                          looking

  **0:45 --  **Break**            
  0:55**                          

  **0:55 --  **Guided Practice**  Personal Card site with teacher guidance
  1:25**                          

  **1:25 --  **Free Practice**    Mini Wikipedia project + stretch goals
  2:45**                          

  **2:45 --  **Wrap-up**          Show-and-tell, seed next session
  3:00**                          
  ---------- -------------------- ----------------------------------------

🎬 **Block 1 --- Demo & Lecture**

*\[40 minutes\]*

**Opening Hook**

*\[5 minutes\]*

Open a browser and visit any well-known website. Ask the class: \"What
just happened between your browser and that computer somewhere in the
world?\" Keep it brief and visual --- browser asks, server answers, that
is the entire model. Flask is the thing that lets their Python code be
the one answering.

**Live Coding --- First App**

*\[15 minutes\]*

-   Create the project folder together, show the minimal structure

-   Write the minimal app.py: import Flask, create the app instance, one
    route returning a string

-   Run flask run in the terminal --- the moment it works in the
    browser, pause and celebrate

-   Turn on debug mode: change the return string, save, refresh ---
    demonstrate the instant feedback loop

  -----------------------------------------------------------------------
  **Tip:** This is the single most important moment of the session. When
  their browser shows text that their Python code produced, the
  connection between back-end and front-end clicks. Do not rush past it.

  -----------------------------------------------------------------------

**The Request/Response Cycle --- Made Visible**

*\[10 minutes\]*

Open browser dev tools, go to the Network tab. Hit the route and watch
the request go out and the response come back. This is not a deep
lecture --- it is simply: \"Look at this tab, see these two things
talking.\"

-   Point out the status code (200) and content type

-   Change the route to something that does not exist --- see the 404
    appear in real time

-   The goal is demystification: the web is just messages going back and
    forth

**Adding More Routes**

*\[10 minutes\]*

-   Add /about and /contact routes, each returning different strings

-   Introduce dynamic routes: /hello/\<name\> using f-strings they
    already know from core Python

-   Show how the variable in the URL becomes a variable in the function
    --- this should feel familiar

⚡ **Mini-Challenge Before Break**

*\[5 minutes\]*

\"Without looking at my screen, add a route /secret that returns a fun
message. You have 2 minutes.\" This ensures every student has typed at
least one route themselves and that their setup is working before the
break.

☕ **Break**

*\[10 minutes\]*

🛠 **Block 2 --- Guided Practice**

*\[30 minutes\]*

**Project: \"Personal Card\" Site**

Students build a small site with teacher guidance. The teacher codes
along on the projector for the first route, then students continue on
their own while the teacher circulates.

**Requirements:**

-   At least 4 routes: home (/), about me, hobbies, and a fun secret
    page

-   Each route returns a different string --- HTML in the strings is
    fine if they want, but not required

-   At least one dynamic route (e.g. /hobby/\<hobby_name\> that responds
    differently per hobby)

-   Encouraged to peek at the Network tab to see their requests
    appearing

  -----------------------------------------------------------------------
  **Tip:** Circulate actively during this block. The students who
  struggle here are usually stuck on file saving, terminal issues, or
  typos in the decorator --- not conceptual problems. Quick fixes keep
  momentum high.

  -----------------------------------------------------------------------

🚀 **Block 3 --- Free Practice**

*\[80 minutes\]*

**Core Challenge: \"Mini Wikipedia\"**

Build a Flask app with at least 6 routes, each about a different topic
the student finds interesting (games, music, sports, anime --- whatever
they want). This gives them repetition with routes while keeping it
personal.

**Requirements:**

-   A home/index route (/) that lists what pages exist

-   At least 6 topic routes with actual content

-   At least one dynamic route

-   Debug mode on for fast iteration

**Stretch Goals (fast finishers):**

-   Add a /random route that uses random.choice() to pick and display a
    random topic

-   Return actual HTML in the strings --- headers, bold, paragraphs ---
    to start feeling the pain of writing HTML inside Python strings

-   Experiment: what happens if two routes have the same URL path?

  -----------------------------------------------------------------------
  **Tip:** The HTML-in-strings stretch goal is strategic. Students who
  try it will get frustrated with the messy code, which creates the
  natural \"aha\" moment for templates in Session 2. If they complain,
  tell them: \"Yeah, this is terrible. We fix it next class.\"

  -----------------------------------------------------------------------

🎯 **Wrap-up**

*\[15 minutes\]*

-   Quick show-and-tell: 2--3 volunteers show their routes in the
    browser

-   Acknowledge common struggles out loud --- normalizes the learning
    process

-   Seed the next class: \"Did anyone get annoyed writing HTML inside
    Python strings? Next class we fix that problem.\"

**Materials & Preparation**

-   **Cheat sheet:** Minimal Flask app boilerplate, \@app.route syntax,
    dynamic route syntax \<variable\>, and how to run the dev server

-   **Troubleshooting guide:** Common errors and fixes --- \"Address
    already in use\" (kill the other process or change port), forgot to
    save before refresh, running flask run from the wrong folder, typos
    in the decorator

-   **Pre-check:** Verify before class that Flask is installed and flask
    run works on at least one test machine. Have a backup plan if a
    student's setup is broken (pair programming with a neighbor).

+-----------------------------------------------------------------------+
| **SESSION 2**                                                         |
|                                                                       |
| **Templates**                                                         |
|                                                                       |
| *Stop Writing HTML in Python --- Jinja2 takes over presentation*      |
+-----------------------------------------------------------------------+

  ----------------------- -----------------------------------------------
  **Duration:** 3 hours   **Goal:** Students move from returning strings
                          to rendering real HTML files, use Jinja2 to
                          inject Python data into pages, and understand
                          why this separation exists.

  ----------------------- -----------------------------------------------

**Time Breakdown**

  ---------- ------------------- ----------------------------------------
  **0:00 --  **Demo & Lecture**  Hook, first template, variables,
  0:45**                         mini-challenge, logic blocks

  **0:45 --  **Break**           
  0:55**                         

  **0:55 --  **Guided Practice** Dynamic Profile Card with teacher
  1:25**                         guidance

  **1:25 --  **Free Practice**   Jinja drill progression: variables →
  2:45**                         lists → conditionals → dicts

  **2:45 --  **Wrap-up**         Show-and-tell, seed next session
  3:00**                         
  ---------- ------------------- ----------------------------------------

🎬 **Block 1 --- Demo & Lecture**

*\[45 minutes\]*

**Opening Hook**

*\[5 minutes\]*

Pull up a student's Mini Wikipedia from last class --- ideally one who
attempted the stretch goal of returning HTML in strings. Show the mess
on the projector: escaped quotes, no syntax highlighting, unreadable
code. Ask: \"Would you want to build a real website like this?\" The
answer sells the lesson.

**The Fix --- First Template**

*\[15 minutes\]*

-   Create the /templates folder --- emphasize this is a Flask
    convention, not optional

-   Move the home page HTML into home.html as a normal HTML file

-   Import render_template and change the route to return
    render_template(\'home.html\')

-   Refresh the browser --- same result, much cleaner code

-   Emphasize: Python does logic, HTML does presentation. They have
    different jobs.

  -----------------------------------------------------------------------
  **Tip:** Write the folder name on the board: templates (with the
  \'s\'). Forgetting the \'s\' or mistyping the filename is the #1 cause
  of TemplateNotFound errors in this session.

  -----------------------------------------------------------------------

**Variables in Templates**

*\[15 minutes\]*

-   Pass data to the template: render_template(\'home.html\',
    name=\'Alice\')

-   In the template: \<h1\>Hello, {{ name }}!\</h1\>

-   Pass multiple variables, including a list, to demonstrate
    flexibility

-   Make it explicit: {{ }} is just \"print this Python thing here\"

-   Live demo: pass current_time using datetime.now() --- students see
    their page update on refresh

⚡ **Mini-Challenge**

*\[5 minutes\]*

\"Create a route /greet/\<name\> that renders a template and shows a
personalized greeting. You have 3 minutes.\" Quick pulse check that
combines everything from Session 1 (dynamic routes) with the new
template concept.

**Logic Blocks**

*\[10 minutes\]*

-   Introduce {% for %} \... {% endfor %} --- loop over a list of
    hobbies

-   Introduce {% if %} / {% else %} / {% endif %} --- show different
    content based on a variable

-   Contrast clearly: {{ }} OUTPUTS, {% %} CONTROLS. Say it twice.

-   Show one gotcha live: forget {% endfor %} and let Jinja yell at them
    with a clear error message

  -----------------------------------------------------------------------
  **Tip:** The {{ }} vs {% %} distinction is the conceptual keystone of
  this session. Write both on the board and draw a line between \"shows
  stuff\" and \"controls stuff.\" Students who internalize this now will
  breeze through inheritance next class.

  -----------------------------------------------------------------------

☕ **Break**

*\[10 minutes\]*

🛠 **Block 2 --- Guided Practice**

*\[30 minutes\]*

**Project: Dynamic Profile Card**

Students build a profile card system that hits every core Jinja concept
in one focused project. Teacher codes along on the projector for the
first profile, then students continue on their own while the teacher
circulates.

**Requirements:**

-   A route /profile/\<username\> that renders a profile template

-   The template receives: a name, an age, a list of hobbies, a favorite
    quote

-   Use {{ }} to display the simple variables

-   Use {% for %} to loop through the hobbies and display them as a list

-   Use {% if %} to show a different message if age is under 18 vs 18+

-   At least 3 hardcoded profiles stored as dicts in the Python file,
    selectable by username

  -----------------------------------------------------------------------
  **Tip:** Most common issues during circulation: forgot to import
  render_template, wrong folder name (\"template\" instead of
  \"templates\"), mixing up {{ }} and {% %}, or missing {% endfor %}/{%
  endif %}. Have these four on a printed cheat sheet ready to hand out.

  -----------------------------------------------------------------------

🚀 **Block 3 --- Free Practice: Jinja Drill Progression**

*\[80 minutes\]*

**Why this block looks different**

From running previous cohorts, we know loops and templating with dicts
are where students most often get stuck. This session's free practice is
a structured drill with progressive difficulty instead of one
open-ended project. Students work through a ladder of small,
self-contained exercises --- each one isolates a single Jinja concept
before combining them. All exercises live in the same Flask app, so by
the end students have one project with many routes.

**How to run it**

-   Hand out a printed list of the exercises (or share a link) so
    students can work at their own pace

-   For every exercise, the Python route signature and the data are
    **given** --- students only write the template side. This isolates
    Jinja practice and removes the \"what data should I invent\"
    friction

-   Expect most students to reach the end of Level 3. Level 4 is the
    stretch zone

-   Circulate heavily during Level 3 (nested if inside for) and Level 4
    (dicts) --- these are the genuine difficulty jumps

  -----------------------------------------------------------------------
  **Tip:** Do not let students skip levels. The whole point is the
  ladder. If someone feels a level is too easy, they finish it in 3
  minutes and move on --- that is fine. But no jumping from Level 1 to
  Level 4.

  -----------------------------------------------------------------------

**Level 1 --- Simple Variables** *(the \"print this here\" stage)*

Only goal: get comfortable with {{ }} and passing variables to
render_template. No loops, no conditionals yet.

-   **1a --- Instagram-style Profile Card.** Route /perfil passes name,
    bio, followers, following, and posts (all hardcoded in Python).
    Template renders a social profile card.

-   **1b --- Product Card (iPhone).** Route /produto passes product
    name, price, description, an image path (from /static/images/), and
    one more field of the student\'s choice. Template renders a product
    page. Key teaching point: **images are just variables too** ---
    pass the path as a string, use it in {{ image }}.

-   **1c --- Order Receipt.** Route /pedido passes item_name, quantity,
    and unit_price. Python **pre-computes** total = quantity \*
    unit_price and passes it too. Template displays a receipt-style
    page: \"3 × Coxinha @ R\$ 8,00 = R\$ 24,00\". Teaching point:
    **Python does the math, the template just displays** --- no logic
    in the HTML.

  -----------------------------------------------------------------------
  **Checkpoint:** Walk the room. Confirm everyone can pass a variable
  and see it on the page. Fix any TemplateNotFound or
  undefined-variable errors before moving on --- these compound later.

  -----------------------------------------------------------------------

**Level 2 --- Lists and `{% for %}`** *(the \"repeat this\" stage)*

Now they meet {% for %}. Data stays as flat lists of strings --- no
dicts yet.

-   **2a --- Candidatos Aprovados.** Route /aprovados passes a list of
    6--8 candidate names (plain strings). Template loops through them
    and renders each as an \<li\> inside a \<ul\>. Simplest possible
    loop.

-   **2b --- Playlist.** Route /playlist passes a list of song names.
    Template renders a numbered list (\<ol\>). Above the list, show
    \"{{ songs\|length }} músicas nessa playlist\" using the \|length
    filter. Introduces the idea that filters exist.

-   **2c --- Netflix Series Rating.** Route /serie passes the series
    name and stars (an int, 1--5). Template uses {% for \_ in
    range(stars) %}⭐{% endfor %} to print that many star emojis. A
    different **kind** of loop --- not iterating over data, but
    repeating N times.

  -----------------------------------------------------------------------
  **Checkpoint:** The big error here is forgetting {% endfor %}. Let
  students hit it once and read Jinja\'s error message before
  intervening. That error-reading skill pays off all course.

  -----------------------------------------------------------------------

**Level 3 --- Conditionals with `{% if %}`** *(the \"decide what to
show\" stage)*

Now conditionals. Still simple variables and flat lists --- no dicts.

-   **3a --- Perfil com Idade.** Route /perfil-idade passes name and
    age (hardcoded, e.g. age = 16). Template shows the name, and uses
    {% if %} / {% else %} to show \"Conteúdo para menores\" if age \<
    18 or \"Conteúdo adulto liberado\" if 18+. Simplest possible if.

-   **3b --- Weather Page.** Route /clima passes temperature (int) and
    city. Template shows the city and uses {% if %} / {% elif %} / {%
    else %} to pick an emoji and message: freezing (\< 10°), nice
    (10--25°), hot (\> 25°). Introduces {% elif %} naturally.

-   **3c --- Extrato Pix. ⚠️ Boss of Level 3.** Route /pix passes a
    list of numbers (transaction values, positive and negative mixed).
    Template loops through them with {% for %}, and **inside** the
    loop uses {% if %} to classify each one: if value \> 0, show in
    green as \"Recebido\"; if value \< 0, show in red as \"Enviado\".
    This is the first **nested** {% if %} inside {% for %} --- exactly
    the combo that trips students up.

  -----------------------------------------------------------------------
  **Checkpoint:** 3c is the hardest conceptual jump so far. Ask two
  students to explain out loud: \"What does the for do? What does the
  if inside it do?\" Verbalizing cements it. If more than a third of
  the room is stuck, pause and do it together on the projector.

  -----------------------------------------------------------------------

**Level 4 --- Dictionaries** *(the \"real data\" stage)*

Now data looks like what it will look like in real projects. Most
students reach here only partially --- that is fine. Level 4 is where
the session\'s stretch value lives.

-   **4a --- Pet Card (one dict).** Route /pet passes a single dict:
    pet = {\"nome\": \"Rex\", \"especie\": \"Cachorro\", \"idade\": 5,
    \"vacinado\": True}. Template accesses {{ pet.nome }}, {{
    pet.especie }}, etc. Only new thing: dot notation on dicts in
    Jinja.

-   **4b --- Sala de Aula (list of dicts).** Route /turma passes a
    list of student dicts, each with nome, idade, nota. Template loops
    and renders a table row per student. The \"real\" pattern: {% for
    aluno in alunos %} then {{ aluno.nome }} inside.

-   **4c --- Loja (list of dicts + conditional).** Route /loja passes
    a list of product dicts, each with nome, preco, em_estoque
    (boolean). Template loops and shows each product, using {% if
    produto.em_estoque %} to show a green \"Disponível\" badge or a
    red \"Esgotado\" badge. The full combo: loop + dict access +
    conditional. This is the exact pattern they will use for CRUD
    listing pages in Sessions 7--8.

-   **4d --- Nested Data. ⚠️ Boss Level.** Route /times passes a list
    of team dicts, each with a nome and a membros list. Template has
    an **outer** loop over teams and an **inner** loop over each
    team\'s members. Genuinely hard --- frame as optional or
    pair-programming. Students who nail this are fully ready for
    Sessions 4--8.

  -----------------------------------------------------------------------
  **Tip:** If a student finishes 4d early, have them go back and add
  CSS to make their pages look nice, or flip the exercise: give them
  a template and have them write the Python route that feeds it the
  right data. That reverse exercise is an excellent real-
  understanding check.

  -----------------------------------------------------------------------

🎯 **Wrap-up**

*\[15 minutes\]*

-   Ask 2--3 volunteers to show one exercise each in the browser ---
    pick different levels so the class sees the full progression

-   Quick pulse: show of hands for \"reached Level 3\" and \"reached
    Level 4\". This tells you where the class landed without singling
    anyone out

-   Reinforce the two big ideas: (1) Python file stays clean, HTML
    file stays clean, (2) {{ }} for output, {% %} for logic

-   Seed next class: \"Every exercise you wrote today has duplicate
    HTML on top --- the same \<head\>, the same \<body\>. Next class
    we fix that with inheritance, and we finally style everything
    with real CSS files.\"

**Materials & Preparation**

-   **Cheat sheet:** render_template syntax, passing variables, {{ }} vs
    {% %}, {% for %} and {% if %} syntax with closing tags highlighted

-   **Error reference:** What TemplateNotFound looks like and how to fix
    it (folder name, file name, typo)

-   **Common mistakes sheet:** Show {{%}} vs {%%} vs {{}} side by side
    --- teenagers mix these up constantly

-   **Pre-check:** Save a student Mini Wikipedia from Session 1 that
    used HTML in strings (with permission) to use as the opening hook

**Pedagogical Notes**

The biggest trap in this session is spending too long on the hook or
theory. The real learning happens when students are writing {{ variable
}} themselves and watching it appear on their page. If the lecture runs
long, cut the logic blocks demo shorter --- they will pick it up in the
guided practice anyway.

For mixed confidence levels: the guided practice gives strugglers a
clear shared path, while the drill progression in the free practice
block handles differentiation automatically --- strugglers consolidate
Levels 1--2, advanced students push into Level 4. Nobody feels stuck
or bored.

Session 3 will introduce base.html and static files. Every drill
exercise from this session is a perfect refactoring target --- same
repeated HTML skeleton across all of them, ready to be collapsed into
one base.html next class.

+-----------------------------------------------------------------------+
| **SESSION 3**                                                         |
|                                                                       |
| **Template Inheritance + Static Files**                               |
|                                                                       |
| *Stop copy-pasting navbars --- and finally, real CSS*                 |
+-----------------------------------------------------------------------+

  ----------------------- -----------------------------------------------
  **Duration:** 3 hours   **Goal:** Students eliminate duplication with
                          base.html and blocks, and link their HTML/CSS
                          knowledge into Flask by serving real
                          stylesheets and images from /static.

  ----------------------- -----------------------------------------------

**Time Breakdown**

  ---------- ------------------- ----------------------------------------
  **0:00 --  **Demo & Lecture**  Inheritance, base.html, blocks, static
  0:45**                         files, url_for

  **0:45 --  **Break**           
  0:55**                         

  **0:55 --  **Guided Practice** Refactor the Session 2 drill exercises
  1:25**                         with inheritance + CSS

  **1:25 --  **Free Practice**   Multi-page portfolio site from scratch
  2:45**                         

  **2:45 --  **Wrap-up**         Show-and-tell, seed next session
  3:00**                         
  ---------- ------------------- ----------------------------------------

🎬 **Block 1 --- Demo & Lecture**

*\[45 minutes\]*

**Opening Hook**

*\[5 minutes\]*

Pull up a student\'s drill exercises from last session --- open two or
three of them side by side (say the Perfil, the Playlist, and the
Extrato Pix templates). Highlight the duplicated parts --- every file
has its own \<head\>, its own \<body\>, no shared nav or footer. Ask:
\"If you wanted one menu bar linking all these pages together, how
many files would you have to edit?\" Now imagine 20 pages. The pain is
real --- and that is exactly what we are fixing today.

**Template Inheritance --- The base.html Pattern**

*\[15 minutes\]*

-   Create base.html with the skeleton: \<!DOCTYPE html\>, \<head\>,
    \<body\>, nav, footer

-   Introduce {% block content %}{% endblock %} as a \"hole\" where
    child pages slot their content

-   Add {% block title %}My Site{% endblock %} inside \<title\> for
    per-page titles

-   Convert home.html to extend base: {% extends \'base.html\' %} and
    fill in {% block content %}\...{% endblock %}

-   Refresh --- same page, but now the header/footer lives in one place

-   Convert the detail page too --- watch how much smaller the files get

-   Live edit: add a link to the nav in base.html, refresh both pages,
    see both update --- this is the magic moment

  -----------------------------------------------------------------------
  **Tip:** Do not skip the live-edit moment. Editing base.html once and
  seeing two child pages update is what makes inheritance click. It is
  the payoff for the whole concept.

  -----------------------------------------------------------------------

⚡ **Mini-Challenge**

*\[5 minutes\]*

\"Add a new page /credits that extends base.html and just has a heading
inside the content block. You have 3 minutes.\" Quick confidence check
that they understand extends and block.

**Static Files --- Connecting CSS At Last**

*\[15 minutes\]*

-   Create the /static folder alongside /templates

-   Create static/css/style.css with something dramatic (big colored
    background) so the change is obvious

-   In base.html, link it: \<link rel=\"stylesheet\" href=\"{{
    url_for(\'static\', filename=\'css/style.css\') }}\"\>

-   Refresh --- the whole site is now styled

-   Explain url_for in one sentence: \"It is Flask\'s way of writing the
    correct path to a file without us guessing.\" Do not over-explain.

-   Show that images work the same way: put an image in static/images/,
    reference it with url_for

**The Key Insight**

*\[5 minutes\]*

Draw on the board or show on screen:

-   /templates → HTML files (Python\'s job to send these)

-   /static → CSS, images, JS (browser fetches these directly)

-   Two different pipelines, one project

☕ **Break**

*\[10 minutes\]*

🛠 **Block 2 --- Guided Practice**

*\[30 minutes\]*

**Project: Refactor the Drill Exercises**

Students take three or four of their drill exercises from Session 2
and unify them under one base.html with shared navigation. The
refactoring approach is deliberate: they are not building something
new, they are making something they already built better. This
reinforces that inheritance is a tool for real-world cleanup, not an
abstract concept.

**Requirements:**

-   Create base.html with a proper skeleton, a nav bar linking to at
    least 3 of the drill routes (e.g. Perfil, Playlist, Pix), and a
    footer

-   Add blocks for title and content

-   Refactor at least 3 drill templates to extend base.html

-   Create static/css/style.css and link it in base.html

-   Add at least 5 CSS rules that actually change the page
    (background, font, spacing, nav styling, anything)

-   Add at least one image from static/images/ somewhere (logo,
    banner, background --- their choice)

  -----------------------------------------------------------------------
  **Tip:** Students who did not finish many drill exercises last class
  should get a barebones handout with 3 pre-written templates (Perfil,
  Playlist, Pix) so they can jump straight into refactoring without
  having to rebuild from scratch. This keeps the whole class on the
  same exercise and avoids anyone falling further behind.

  -----------------------------------------------------------------------

Most common issues during circulation: forgetting to save the CSS file,
typos in url_for, missing quotes around \'css/style.css\', or the
browser caching the old CSS. Teach them Ctrl+Shift+R for a hard refresh
--- it will save hours across the rest of the course.

🚀 **Block 3 --- Free Practice**

*\[80 minutes\]*

**Core Challenge: Multi-Page Portfolio Site**

Build a personal portfolio from scratch. This cements inheritance,
static files, and previous concepts (loops, variables, dynamic content)
into one cohesive piece --- and it is something they can actually show
to family and friends. Motivation matters.

**Requirements:**

-   At least 4 pages: Home, About, Projects, Contact

-   All pages extend a shared base.html with a nav bar linking to all
    four

-   A linked external CSS file in static/css/

-   At least one image served from static/images/

-   Each page uses {% block title %} to set its own browser tab title

-   The Projects page loops through a list of project dicts passed from
    Python (name + description + optional image)

**Stretch Goals (fast finishers):**

-   Add a second block like {% block extra_css %} for page-specific
    styles

-   Use {% if %} in the nav to highlight the current page (requires
    passing a current_page variable from each route)

-   Add a Google Font via a \<link\> in base.html and apply it in the
    CSS

-   Make the portfolio responsive with basic CSS (mobile-friendly nav,
    flex layouts)

  -----------------------------------------------------------------------
  **Tip:** Watch out for students who get too deep into CSS and spend the
  whole free practice tweaking colors without finishing all four pages.
  Gentle nudge: \"Get all four pages working first, then make them
  pretty.\"

  -----------------------------------------------------------------------

🎯 **Wrap-up**

*\[15 minutes\]*

-   2--3 volunteers show their portfolios --- celebrate the visual
    polish, this is the first session where results look like a \"real
    website\"

-   Reinforce: base.html + {% block %} is one of the most useful
    patterns in this course. They will use it in every Flask project,
    forever.

-   Seed next class: \"Right now your sites just SHOW stuff. Next class,
    your users will be able to TYPE stuff back to you --- we are
    building forms.\"

**Materials & Preparation**

-   **Cheat sheet:** base.html skeleton template, {% extends %} syntax,
    {% block %} syntax, url_for(\'static\', filename=\'\...\') with
    quotes highlighted

-   **Starter CSS file:** A few pre-written rules students can copy as a
    starting point --- especially helpful for students whose CSS
    confidence is shaky from the crash course

-   **Barebones drill templates handout:** 3 minimal working templates
    from Session 2 (e.g. Perfil, Playlist, Pix) for students who missed
    the last class or did not finish, so they can jump straight into
    refactoring without rebuilding from scratch

-   **Troubleshooting guide:** \"My CSS isn\'t showing up\" → check
    folder name, check url_for quotes, hard refresh with Ctrl+Shift+R

**Pedagogical Notes**

This is the first session where their work LOOKS like real websites,
which is a massive motivation boost. Do not undercut it with too much
lecture. If a student finishes everything, encourage them to spend time
actually designing (colors, spacing, images) rather than jumping to the
next conceptual thing. The aesthetic reward of CSS working is what
cements the session emotionally.

The url_for function will appear again and again throughout the course
(for linking routes, for static files, for redirects). Do not
over-explain it now --- treat it as \"the right way to reference things
in Flask\" and let familiarity build across sessions.

The hard-refresh tip (Ctrl+Shift+R) pays dividends for the rest of the
course. Teach it deliberately, write it on the board, and bring it up
again any time a student says \"my changes aren\'t showing up.\"
