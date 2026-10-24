#!/usr/bin/env python3
"""Erzeugt Worklist + Update-Payloads für den Audio-Lauf '04 - Musik & Kunst' (08.10.2026).

Datenbasis: verifizierte Live-Read-backs dieser Session (nach Phase 2 + Phase 3).
- Worklist: session-notizen/2026-10-08_04-musik-kunst_audio-worklist.jsonl
- Payloads: session-notizen/2026-10-08_04-musik-kunst_audio-payloads.json
Regeln: Anki-MCP-Verwendung.md §1.3 (Split nur am getaggten Trenner), §1.4 (Zwei-Paar),
§2 (Dateinamen: kleingeschrieben, Satzzeichen entfernt, Umlaute bleiben, _bsp2 für
zweites Satzpaar, 6-stelliges Kleinbuchstaben-/Ziffern-Suffix).
"""
import json
import random
import re

NOTES = [
    (1784870727164, "das Lied", "Цю пісню я знаю ще з дитинства.<br><br>Dieses Lied kenne ich schon aus meiner Kindheit."),
    (1784870727168, "das Instrument", "На якому інструменті ти найбільше любиш грати?<br><br>Welches Instrument spielst du am liebsten?"),
    (1784870727172, "singen", "Вона щовечора співає пісню перед сном.<br><br>Sie singt jeden Abend zum Einschlafen ein Lied."),
    (1784870727176, "das Konzert", "Минулого тижня ми разом були на концерті.<br><br>Wir waren letzte Woche zusammen auf einem Konzert."),
    (1784870727180, "der Chor", "Моя донька співає в дитячому хорі.<br><br>Meine Tochter singt in einem Kinderchor."),
    (1784870727184, "die Melodie", "Ця мелодія вже кілька днів не виходить мені з голови.<br><br>Die Melodie geht mir seit Tagen nicht aus dem Kopf."),
    (1784870727188, "tanzen", "На весіллі всі танцювали до пізньої ночі.<br><br>Auf der Hochzeit haben alle bis spät in die Nacht getanzt."),
    (1784870727192, "der Tanz", "Цей танець походить ще з ХІХ століття.<br><br>Dieser Tanz stammt ursprünglich aus dem 19. Jahrhundert."),
    (1784870727196, "die Gitarre", "Він грає на гітарі ще зі шкільних часів.<br><br>Er spielt seit der Schulzeit Gitarre."),
    (1784870727200, "das Klavier", "Моя донька вже два роки вчиться грати на фортепіано.<br><br>Meine Tochter lernt seit zwei Jahren Klavier."),
    (1784870727204, "die Geige", "Скрипка вважається одним із найскладніших інструментів.<br><br>Die Geige gilt als eines der schwierigsten Instrumente."),
    (1784870727208, "der Musiker / die Musikerin", "Минулого тижня музикант представив свій новий альбом.<br><br>Der Musiker hat sein neues Album letzte Woche vorgestellt.<br><br>Музикантка вже п’ять років грає в джазовому гурті.<br><br>Die Musikerin spielt seit fünf Jahren in einer Jazzband."),
    (1784870727212, "das Album", "Її новий альбом зараз дуже успішний у чартах.<br><br>Ihr neues Album ist gerade in den Charts sehr erfolgreich."),
    (1784870727216, "das Festival", "Щоліта в місті відбувається музичний фестиваль.<br><br>Jeden Sommer findet in der Stadt ein Musikfestival statt."),
    (1784870727220, "die Bühne", "На сцені стояв молодий, невідомий ансамбль.<br><br>Auf der Bühne stand ein junges, unbekanntes Ensemble."),
    (1784870727224, "das Genre", "Його музичний смак охоплює багато різних жанрів.<br><br>Sein Musikgeschmack umfasst viele verschiedene Genres."),
    (1784870727228, "der Text", "Текст пісні я ще не до кінця розумію.<br><br>Den Text des Liedes verstehe ich noch nicht ganz."),
    (1784870727232, "das Radio", "Вранці за сніданком я завжди слухаю радіо.<br><br>Morgens höre ich beim Frühstück immer Radio."),
    (1784870727236, "die Playlist", "Для поїздки машиною вона створила новий плейлист.<br><br>Für die Autofahrt hat sie eine neue Playlist erstellt."),
    (1784870727240, "der Rhythmus", "Від ритму цієї пісні одразу хочеться танцювати.<br><br>Der Rhythmus dieses Liedes lädt sofort zum Tanzen ein."),
    (1784870727244, "die Stimme", "У неї дуже сильний співочий голос.<br><br>Sie hat eine sehr kräftige Singstimme."),
    (1784870727248, "die Band", "На вихідних гурт виступає в невеликому клубі.<br><br>Die Band tritt am Wochenende in einem kleinen Club auf."),
    (1784870727252, "das Musikvideo", "Нове музичне відео вже подивилися мільйони разів.<br><br>Das neue Musikvideo wurde schon millionenfach angesehen."),
    (1784870727256, "auftreten", "У суботу співачка вперше виступає наживо.<br><br>Die Sängerin tritt am Samstag zum ersten Mal live auf."),
    (1784870727260, "das Musikinstrument", "У школі можна спробувати грати на різних музичних інструментах.<br><br>In der Schule kann man verschiedene Musikinstrumente ausprobieren."),
    (1784870727268, "das Publikum", "Публіка довго аплодувала.<br><br>Das Publikum hat lange applaudiert."),
    (1784870727272, "der Klang", "Цей інструмент має зовсім особливе звучання.<br><br>Dieses Instrument hat einen ganz besonderen Klang."),
    (1784870727276, "improvisieren", "Добрі джазові музиканти вміють чудово імпровізувати.<br><br>Gute Jazzmusiker können sehr gut improvisieren."),
    (1784870727280, "die Note (Musik)", "Без нот, на жаль, вона не може зіграти цю п’єсу.<br><br>Ohne Noten kann sie das Stück leider nicht spielen."),
    (1784870727284, "malen", "У дитинстві він любив малювати акварельними фарбами.<br><br>Als Kind hat er gern mit Wasserfarben gemalt."),
    (1784870727288, "das Gemälde", "Ця картина вже багато років висить у вітальні.<br><br>Das Gemälde hängt seit Jahren im Wohnzimmer."),
    (1784870727292, "sticken", "Бабуся навчила мене вишивати.<br><br>Meine Großmutter hat mir das Sticken beigebracht."),
    (1784870727296, "die Stickerei", "Вишивка на сорочці тривала кілька тижнів.<br><br>Die Stickerei auf dem Hemd hat mehrere Wochen gedauert."),
    (1784870727300, "die Töpferei", "У цьому маленькому музеї можна помилуватися традиційним гончарством.<br><br>In dem kleinen Museum kann man traditionelle Töpferei bewundern."),
    (1784870727304, "das Handwerk", "Багато старих ремесел сьогодні підтримують лише поодинокі люди.<br><br>Viele alte Handwerke werden heute nur noch von wenigen Menschen gepflegt."),
    (1784870727308, "zeichnen", "У вільний час він любить малювати портрети олівцем.<br><br>Er zeichnet in seiner Freizeit gern Porträts."),
    (1784870727312, "die Zeichnung", "Цей малюнок вона зробила ще в дитинстві.<br><br>Diese Zeichnung hat sie schon als Kind angefertigt."),
    (1784870727316, "die Ausstellung", "Виставка в музеї показує твори ХХ століття.<br><br>Die Ausstellung im Museum zeigt Werke aus dem 20. Jahrhundert."),
    (1784870727320, "der Künstler / die Künstlerin", "Митець зазвичай працює у власній маленькій майстерні.<br><br>Der Künstler arbeitet meist in seinem eigenen kleinen Atelier.<br><br>Мисткиня влітку виставляє свої картини.<br><br>Die Künstlerin stellt ihre Bilder im Sommer aus."),
    (1784870727324, "die Skulptur", "На площі стоїть відома бронзова скульптура.<br><br>Auf dem Platz steht eine bekannte Skulptur aus Bronze."),
    (1784870727328, "die Ausbildung (künstlerisch)", "Для професії митця класична освіта не є обов’язковою.<br><br>Für den Beruf des Künstlers ist keine klassische Ausbildung vorgeschrieben."),
    (1784870727332, "kreativ", "Вона дуже креативна людина і з задоволенням пробує нове. <i>oder</i> Вона дуже творча людина і з задоволенням пробує нове.<br><br>Sie ist ein sehr kreativer Mensch und probiert gern Neues aus."),
    (1784870727336, "das Material", "Для вишивки потрібні спеціальний матеріал і нитки.<br><br>Für die Stickerei braucht man spezielles Material und Garn."),
    (1784870727340, "das Muster", "Кожен візерунок на вишивці розповідає власну історію.<br><br>Jedes Muster auf der Stickerei erzählt eine eigene Geschichte."),
    (1784870727344, "das Kunsthandwerk", "На ринку багато місцевого художнього ремесла.<br><br>Auf dem Markt gibt es viel Kunsthandwerk aus der Region."),
    (1784870727348, "die Handarbeit", "Ця скатертина — суто ручна робота.<br><br>Diese Tischdecke ist reine Handarbeit."),
    (1784870727352, "der Pinsel", "Для цієї картини вона використовувала дуже тонкі пензлі.<br><br>Für dieses Gemälde hat sie sehr feine Pinsel benutzt."),
    (1784870727356, "die Farbe", "Він завжди змішує свої фарби сам.<br><br>Er mischt seine Farben immer selbst."),
    (1784870727360, "die Leinwand", "Цю картину намальовано на великому полотні.<br><br>Das Bild wurde auf einer großen Leinwand gemalt."),
    (1784870727364, "das Atelier", "Мисткиня працює в маленькій майстерні на околиці міста.<br><br>Die Künstlerin arbeitet in einem kleinen Atelier am Stadtrand."),
    (1784870727368, "die Schnitzerei", "У деяких регіонах різьблення по дереву — старовинне ремесло.<br><br>Die Holzschnitzerei ist in manchen Regionen ein altes Handwerk."),
    (1784870727372, "das Kunstwerk", "Цей твір мистецтва вже багато років висить у музеї.<br><br>Dieses Kunstwerk hängt seit Jahren im Museum."),
    (1784870727376, "die Galerie", "У старому місті є невелика, але чудова галерея.<br><br>In der Altstadt gibt es eine kleine, aber feine Galerie."),
    (1784870727380, "gestalten", "Весільні запрошення вона оформлює сама. <i>oder</i> Весільні запрошення вона створює сама.<br><br>Sie gestaltet die Einladungskarten für die Hochzeit selbst."),
    (1784870727384, "das Talent für Kunst", "Ще в дитинстві він виявляв великий хист до мистецтва.<br><br>Schon als Kind zeigte er ein großes Talent für Kunst."),
    (1784870727388, "die Keramikwerkstatt", "У гончарній майстерні можна самостійно виготовити миски.<br><br>In der Keramikwerkstatt kann man Schalen selbst töpfern."),
    (1784870727392, "die Verzierung", "Оздоблення великоднього яйця часто триває кілька годин.<br><br>Die Verzierung des Ostereis dauert oft mehrere Stunden."),
    (1784870727396, "die Symbolik", "Кожен колір у вишивці має власну символіку.<br><br>Jede Farbe hat in der Stickerei eine eigene Symbolik."),
    (1784870727400, "die Bandura", "Бандура — це щипковий інструмент, що має до 65 струн, і вважається найвідомішим українським народним інструментом.<br><br>Die Bandura ist ein Zupfinstrument mit bis zu 65 Saiten und gilt als das bekannteste ukrainische Volksinstrument."),
    (1784870727404, "die Vyshyvanka", "Вишиванка — вишита сорочка — донині є важливим символом української ідентичності.<br><br>Die Vyshyvanka, ein bestickstes Hemd, ist bis heute ein wichtiges Symbol ukrainischer Identität."),
    (1784870727408, "das Volkslied", "У Німеччині народні пісні сьогодні виконують переважно в товариствах та на святах.<br><br>In Deutschland werden Volkslieder heute vor allem noch in Vereinen und bei Festen gepflegt."),
    (1784870727412, "das Pysanka", "Розписування великодніх яєць, відомих як писанки, — багатовікове українське художнє ремесло.<br><br>Das Verzieren von Ostereiern, Pysanky genannt, ist ein jahrhundertealtes ukrainisches Kunsthandwerk."),
    (1784870727416, "der Nationaltanz", "Гопак вважається національним танцем України та відомий своїми акробатичними стрибками.<br><br>Der Hopak gilt als Nationaltanz der Ukraine und ist bekannt für seine akrobatischen Sprünge."),
    (1784870727420, "die Volkskunst", "Українське народне мистецтво охоплює, крім вишивки та кераміки, також розписування великодніх яєць.<br><br>Die ukrainische Volkskunst umfasst neben Stickerei und Keramik auch das Verzieren von Ostereiern."),
    (1784870727424, "der Chorgesang", "Багатоголосий хоровий спів відіграє центральну роль в українській народній музиці.<br><br>Der mehrstimmige Chorgesang spielt in der ukrainischen Volksmusik eine zentrale Rolle."),
    (1784870727428, "der Komponist / die Komponistin", "Миколу Лисенка вважають засновником професійної української композиторської школи.<br><br>Mykola Lyssenko gilt als Begründer der professionellen ukrainischen Komponistenschule.<br><br>Музику до фільму композиторка пише сама.<br><br>Die Komponistin schreibt die Musik für den Film selbst."),
    (1784870727432, "die Trombita", "Трембіта — дерев’яний духовий інструмент завдовжки близько трьох метрів — традиційно використовувалася в Карпатах.<br><br>Die Trombita, ein etwa drei Meter langes Holzblasinstrument, wurde traditionell in den Karpaten genutzt."),
    (1784870727436, "die Keramik", "Крім вишивки, до українського народного мистецтва належить і традиційна кераміка.<br><br>Neben Stickerei zählt auch traditionelle Keramik zur ukrainischen Volkskunst."),
    (1784870727440, "die Trachtenkleidung", "У Німеччині народний костюм носять передусім у Баварії на народних святах.<br><br>In Deutschland wird Trachtenkleidung vor allem in Bayern zu Volksfesten getragen."),
    (1791479150612, "die Aufführung", "Вистава тривала майже дві години.<br><br>Die Aufführung dauerte fast zwei Stunden."),
    (1791479150613, "der Auftritt", "Її перший виступ мав великий успіх.<br><br>Ihr erster Auftritt war ein großer Erfolg."),
]

TWO_PAIR = {1784870727208, 1784870727320, 1784870727428}


def basename(front: str) -> str:
    return re.sub(r"[^a-zäöüß0-9]", "", front.lower())


def clean_text(seg: str) -> str:
    t = re.sub(r"<[^>]+>", " ", seg)
    return re.sub(r"\s+", " ", t).strip()


alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
used: set = set()


def suffix() -> str:
    while True:
        s = "".join(random.choice(alphabet) for _ in range(6))
        if s not in used:
            used.add(s)
            return s


worklist = []
payloads = {}
for nid, front, example in NOTES:
    base = basename(front)
    if nid in TWO_PAIR:
        parts = [p.strip() for p in example.split("<br><br>")]
        assert len(parts) == 4, (nid, parts)
        uk1, de1, uk2, de2 = parts
        n1 = f"{base}_bsp_{suffix()}.mp3"
        n2 = f"{base}_bsp2_{suffix()}.mp3"
        worklist.append({"id": nid, "file": f"mp3/{n1}", "uk": clean_text(uk1)})
        worklist.append({"id": nid, "file": f"mp3/{n2}", "uk": clean_text(uk2)})
        payloads[str(nid)] = {
            "front": front,
            "example": f"[sound:{n1}]<br><br>{uk1}<br><br>{de1}<br><br>[sound:{n2}]<br><br>{uk2}<br><br>{de2}",
        }
    else:
        head = example.split("<br>")[0]
        if "<i>oder</i>" in head:  # Split nur am getaggten Trenner (§1.3)
            head = head.split("<i>oder</i>")[0]
        uk = clean_text(head)
        n1 = f"{base}_bsp_{suffix()}.mp3"
        worklist.append({"id": nid, "file": f"mp3/{n1}", "uk": uk})
        payloads[str(nid)] = {
            "front": front,
            "example": f"[sound:{n1}]<br><br>{example.strip()}",
        }

assert len(NOTES) == 71, len(NOTES)
assert len(worklist) == 74, len(worklist)
assert len({w["file"] for w in worklist}) == 74

wl_path = "session-notizen/2026-10-08_04-musik-kunst_audio-worklist.jsonl"
pl_path = "session-notizen/2026-10-08_04-musik-kunst_audio-payloads.json"
with open(wl_path, "w", encoding="utf-8") as f:
    for w in worklist:
        f.write(json.dumps(w, ensure_ascii=False) + "\n")
with open(pl_path, "w", encoding="utf-8") as f:
    json.dump(payloads, f, ensure_ascii=False, indent=1)

print(f"NOTES={len(NOTES)} WORKLIST={len(worklist)} (2-Paar: {sorted(TWO_PAIR)})")
for w in worklist:
    print(w["file"], "|", w["uk"][:70])
