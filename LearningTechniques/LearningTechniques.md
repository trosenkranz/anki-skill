# Learning Techniques with AI

> **Source:** YouTube video transcript ("Transkript.txt") by **Trevor Baset**, math professor.
> Topic: How to learn effectively in the AI era — five framework principles for using AI without harming your learning.

---

## 1. Overview

The professor opens with an accidental educational experiment in his second-year linear algebra course:
one homework problem had a one-line solution via a specialized, higher-level formula — the kind of
formula you would not find in the textbook, class notes, or easily on Google/YouTube, **but which AI
would readily provide**. About **42 % of the class used exactly this formula** — and those students
scored on average **22 percentage points worse on the midterm**, turning a healthy passing average
into a failing one. In education research, an effect of that size is enormous; the professor notes he
has never been able to move grades by anything close to that, no matter what he does as a teacher.

His core worry: **students offload the hard parts of thinking** — trying problems, reasoning, struggling —
which is precisely the work that builds problem-solving ability. Reading an AI (or YouTube) solution
and nodding along ("yes, that makes sense") is far easier than producing the solution yourself,
but the *hard work* is where learning happens. This matches larger studies: **task performance can go up
with AI, while long-term retention on later summative assessments drops**.

**Important caveats stated in the video:**

- The goal is **not to moralize** about AI use or shame students. The only question is: which
  strategies are effective for long-term learning?
- Bigger societal questions (what to teach, how to assess, AI and the job market) are set aside.
  The practical question is: *you are stuck in a course with an exam to pass — how can AI be used
  in ways that help rather than hurt?*

---

## 2. The Five Techniques (Extracted & Summarized)

| # | Technique | One-line summary |
|---|-----------|------------------|
| 1 | **Active vs. Passive Learning** | Use AI as an *active* learner: try the problem first, ask only for small hints, evaluate and rephrase the answer yourself. |
| 2 | **Tutoring Techniques** | Prompt the AI like a good human tutor: diagnose, don't hand out answers; ask for small nudges so you do the thinking. |
| 3 | **Learning Goals vs. Friction** | Be intentional about which "friction" you remove — much of the struggle *is* the learning. |
| 4 | **Self-Assessing** | Regularly test yourself (recall, not just recognition); have the AI quiz you; space it out over time. |
| 5 | **Being Critically Reflective** | Scrutinize AI answers: Is it accurate? Is it efficient? Do I understand the rationale? Is it pitched at the right level? |

---

## 3. Detailed Elaboration & Research Enrichment

### Tip 1 — Active vs. Passive Learning

**What the video says**

- *Passive learning*: consuming content someone else created — listening to a professor, watching a
  YouTube video, reading solutions (AI-generated or textbook).
- *Active learning*: you are "in the driver's seat" — problem solving, deciding what to do next,
  testing hypotheses, playing around.
- Active learning is frustrating, slow, and can make you "feel like an idiot"; passive learning
  *feels* good ("that makes sense, that makes sense…"). But the literature is very clear:
  **active learning is far more beneficial**.
- The danger of AI: it makes slipping into passivity effortless, because it serves up so many
  answers you can just read through and copy.
- **Concrete workflow suggested in the video:**
  1. Try the problem yourself first.
  2. Ask the AI for **a small hint** to get moving, just a little bit forward.
  3. **Assess the validity** of what the AI wrote.
  4. **Reinterpret it in your own context and your own words** — make sense of it in your mind.
  5. Be the center of your own learning.

**Research enrichment**

- Freeman et al. (2014), a meta-analysis of 225 studies in PNAS (*"Active learning increases student
  performance in science, engineering, and mathematics"*), found active learning raised exam scores
  by ~6 % (≈ 0.5 SD) and cut failure rates from 34 % to 22 % — students in traditional lectures were
  **1.5× more likely to fail**. This is one of the most robust findings in education research.
- The video author's own classroom result (AI users ≈ 22 points worse on the midterm) is a
  textbook illustration of passive AI consumption: the AI supplied a solution, the reading of it
  *felt* like understanding, but no durable skill was built.

### Tip 2 — Tutoring Techniques (Use AI as a Tutor, Not an Answer Machine)

**What the video says**

- Some papers show AI producing *positive* learning gains — those implementations typically use the
  AI as a **tutor**.
- The professor's best teaching happens one-on-one in office hours and math help centers. Tutoring
  is extremely powerful, but **logistically expensive** — AI may make it scalable.
- Crucially: **tutoring is not about giving answers.** When training tutors, the first rule is:
  don't hand over the solution. Instead:
  - Ask the student to show what they have already tried.
  - **Diagnose** where the actual misunderstanding is.
  - Give **small nudges** so the student accomplishes as much of the thinking as possible on their own.
- **Concrete prompt pattern from the video:** *"Here is a dump of everything I know about this
  problem and what I've tried so far. Give me just a small hint in the right direction, or diagnose
  where I'm missing something."* — prompting this way turns the AI into an effective tutor that
  supports active learning.

**Research enrichment**

- Bastani et al. (2024, PNAS: *"Generative AI without guardrails can harm learning"*): field
  experiment with ~1,000 Turkish high-school math students. Access to a plain GPT-4 chatbot
  ("GPT Base") improved practice performance by **48 %** — but when access was removed, those
  students scored **17 % *worse*** on exams than students who never had access. A second version,
  "GPT Tutor", was **prompted with pedagogical guardrails** (hints, not full solutions): it boosted
  practice performance by 127 % while **largely eliminating the negative exam effect**. This is
  direct, large-scale evidence for exactly the tutoring style the video advocates.
- Kestin, Miller et al. (Harvard, published 2025 in *Scientific Reports*): ~194 physics students
  using a custom AI tutor designed around research-based pedagogy (guiding questions, active
  engagement, no just-giving-answers) **learned roughly twice as much** per lesson as peers in an
  already well-taught *active-learning* classroom, in less time — with **double the engagement**
  and higher motivation. Well-designed AI tutoring can genuinely outperform.

### Tip 3 — Learning Goals vs. Friction (Desirable Difficulties)

**What the video says**

- Be **intentional** about what is a *learning goal* and what is merely *unnecessary friction*.
  Removing inefficiencies is fine — but **a lot of the friction is where the magic of learning happens**.
- Illustrative example: you forgot a formula. Options: Google it, ask the AI, or flip through your
  **handwritten** notes. Flipping through notes feels tedious — but while searching you *think*:
  "it wasn't that week… it came after that topic… ah, here it is, and I remember *why* we derived it."
  In doing so you performed real thinking and **scaffolded the formula into the right spot in your
  mental hierarchy** of knowledge.
- Removing friction can quietly remove learning. The point is not "never Google a formula" — it is
  to notice when friction-removal costs you learning, and to make up for it deliberately.
- Side note from the video: he says *handwritten* notes deliberately — the literature finds
  handwriting more effective than typing precisely because it is slower and less efficient.

**Research enrichment**

- **Desirable difficulties** (Robert & Elizabeth Bjork, UCLA): conditions that make practice harder
  and feel less productive often produce *more* long-term retention and transfer, while easy,
  fluent conditions create an "illusion of mastery". Friction is often cognitively productive.
- Handwritten notes: Mueller & Oppenheimer (2014, *Psychological Science*, "The Pen Is Mightier Than
  the Keyboard") found longhand note-takers outperformed laptop note-takers on conceptual questions,
  presumably because summarizing/slowing forces deeper processing. *(Fairness note: later
  replication attempts, e.g. Urry et al. 2021, have produced mixed results — treat this as
  plausible but not settled.)*

### Tip 4 — Self-Assessing (Possibly the Most Important Tip)

**What the video says**

- Humans are **bad at judging their own understanding**. Countless students: "I thought I understood
  everything, then I failed the exam." There is a disconnect between *felt* understanding and
  *actual* understanding.
- Remedy: constantly **pepper yourself with opportunities to self-assess**:
  - Can you **recall** a basic fact from memory (not just recognize it)?
  - Key distinction: **recognition vs. recollection**. When someone yells "Steve!" and you go
    "Oh yes, of course, Steve!" — that's recognition, which is cognitively much easier than
    producing the name yourself. Exams demand recollection, so practice recollection.
  - Practice **explaining** more complex facts — can you articulate *why* they are true?
  - Do this **regularly and spaced out over time**.
- AI's positive role here: it is **good at generating self-assessment prompts** — have it quiz you,
  then check whether you can perform **unsupported**, sitting back with no notes and no AI.

**Research enrichment**

- **Retrieval practice / testing effect** (Roediger & Karpicke, 2006, *Psychological Science* and
  follow-ups): actively retrieving information from memory produces dramatically better long-term
  retention than re-reading or re-studying — even though re-studying *feels* more effective.
  This is the single best-supported study technique in cognitive psychology.
- **Spaced repetition** (from Ebbinghaus's forgetting curve to modern tools like Anki — note the
  folder you are reading this in): reviewing material at increasing intervals beats massed practice
  ("cramming") for durable memory.
- Recognition vs. recall is a classic memory distinction; testing your *recall* (closed book,
  closed AI) is the honest probe of exam-ready knowledge.

### Tip 5 — Being Critically Reflective

**What the video says**

- AI is "pretty good these days" at first- and second-year math problems — but **not infallible**.
  So read and analyze every answer critically:
  - **Is this needed?** AI often pads solutions with extra fluff.
  - **Is this accurate?** There is always some uncertainty about correctness.
  - **Can I understand the rationale** behind each element of the solution?
- Also watch the **level match**: you may get a *correct* answer built on tools that have nothing
  to do with your course. His students pulled in advanced formulas that "worked" but bypassed the
  course's actual content — fine occasionally, but be careful to keep the right mix between you,
  the audience, and what you receive.
- Critical reflection applies to professors and textbooks too — but it is **doubly important with
  AI**, where both *accuracy* and *efficiency/appropriateness* of answers are uncertain.

**Research enrichment**

- LLM "hallucinations" and plausible-but-wrong reasoning are well documented; domain studies show
  accuracy varies widely by topic and difficulty, which is exactly why "is this accurate?" and
  "do I understand why?" are non-negotiable checks.
- The Bastani et al. study again supports this: students used GPT-4 as a *crutch* — accepting
  answers without verification — and paid for it on exams. Critical scrutiny is the antidote.

---

## 4. Bottom Line (The Video's Conclusion)

- Whether or not to use AI for learning is left as a **personal choice**; the professor himself has
  a "mixture of worry and excitement" and uses AI in some ways, avoids it in others.
- The takeaway: if you use AI, use it **actively** (you do the thinking first), **as a tutor**
  (hints and diagnosis, not solutions), **intentionally about friction** (keep the productive
  struggle), **with constant self-assessment** (recall, explain, space it out), and **critically
  reflective** (accuracy, efficiency, level, rationale).

**Quick self-check before submitting any AI-assisted homework:** Can I sit back, with no notes and
no AI, and re-derive or explain the solution in my own words? If not, I haven't learned it yet —
the AI has.

---

## 5. Key References

**From the transcript (the author's own observations):**
- Unintended classroom experiment: 42 % AI-formula users scored 22 percentage points lower on the midterm (linear algebra).
- Consistent with large studies: AI raises task performance but can lower long-term retention on summative assessments.

**External research cited for enrichment:**
1. Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2024/2025). *Generative AI without guardrails can harm learning: Evidence from high school mathematics.* PNAS. — <https://scale.stanford.edu/publications/generative-ai-can-harm-learning>
2. Freeman, S., et al. (2014). *Active learning increases student performance in science, engineering, and mathematics.* PNAS. — <https://www.pnas.org/doi/10.1073/pnas.1319030111>
3. Kestin, G., Miller, K., et al. (2025). *AI tutoring outperforms in-class active learning.* Scientific Reports. Coverage: <https://news.harvard.edu/gazette/story/2024/09/professor-tailored-ai-tutor-to-physics-course-engagement-doubled/>
4. Mueller, P. A., & Oppenheimer, D. M. (2014). *The Pen Is Mightier Than the Keyboard.* Psychological Science. — <https://journals.sagepub.com/doi/abs/10.1177/0956797614524581>
5. Roediger, H. L., & Karpicke, J. D. (2006). *Test-Enhanced Learning: Taking Memory Tests Improves Long-Term Retention.* Psychological Science. — <https://www.science.org/doi/10.1126/science.1152408> (related retrieval-practice work)
6. Bjork, R. A., & Bjork, E. L. — *Desirable Difficulties Perspective on Learning.* — <https://bjorklab.psych.ucla.edu/>
