# thx https://meta.wikimedia.org/wiki/Stop_word_list/google_stop_word_list


def get_stop_words(language):
    if language == "en":
        return [
            "a",
            "about",
            "above",
            "after",
            "again",
            "against",
            "all",
            "am",
            "an",
            "and",
            "any",
            "are",
            "aren't",
            "as",
            "at",
            "be",
            "because",
            "been",
            "before",
            "being",
            "below",
            "between",
            "both",
            "but",
            "by",
            "can't",
            "cannot",
            "could",
            "couldn't",
            "did",
            "didn't",
            "do",
            "does",
            "doesn't",
            "doing",
            "don't",
            "down",
            "during",
            "each",
            "few",
            "for",
            "from",
            "further",
            "had",
            "hadn't",
            "has",
            "hasn't",
            "have",
            "haven't",
            "having",
            "he",
            "he'd",
            "he'll",
            "he's",
            "her",
            "here",
            "here's",
            "hers",
            "herself",
            "him",
            "himself",
            "his",
            "how",
            "how's",
            "i",
            "i'd",
            "i'll",
            "i'm",
            "i've",
            "if",
            "in",
            "into",
            "is",
            "isn't",
            "it",
            "it's",
            "its",
            "itself",
            "let's",
            "me",
            "more",
            "most",
            "mustn't",
            "my",
            "myself",
            "no",
            "nor",
            "not",
            "of",
            "off",
            "on",
            "once",
            "only",
            "or",
            "other",
            "ought",
            "our",
            "ours",
            "ourselves",
            "out",
            "over",
            "own",
            "same",
            "shan't",
            "she",
            "she'd",
            "she'll",
            "she's",
            "should",
            "shouldn't",
            "so",
            "some",
            "such",
            "than",
            "that",
            "that's",
            "the",
            "their",
            "theirs",
            "them",
            "themselves",
            "then",
            "there",
            "there's",
            "these",
            "they",
            "they'd",
            "they'll",
            "they're",
            "they've",
            "this",
            "those",
            "through",
            "to",
            "too",
            "under",
            "until",
            "up",
            "very",
            "was",
            "wasn't",
            "we",
            "we'd",
            "we'll",
            "we're",
            "we've",
            "were",
            "weren't",
            "what",
            "what's",
            "when",
            "when's",
            "where",
            "where's",
            "which",
            "while",
            "who",
            "who's",
            "whom",
            "why",
            "why's",
            "with",
            "won't",
            "would",
            "wouldn't",
            "you",
            "you'd",
            "you'll",
            "you're",
            "you've",
            "your",
            "yours",
            "yourself",
            "yourselves",
        ]
    elif language == "fr":
        return [
            "alors",
            "au",
            "aucuns",
            "aussi",
            "autre",
            "avant",
            "ave",
            "avoir",
            "bon",
            "car",
            "ce",
            "cela",
            "ces",
            "ceux",
            "chaque",
            "ci",
            "comme",
            "comment",
            "d",
            "des",
            "du",
            "dedans",
            "dehors",
            "depuis",
            "deux",
            "devrait",
            "doit",
            "donc",
            "dos",
            "droite",
            "début",
            "elle",
            "elles",
            "en",
            "encore",
            "essai",
            "est",
            "et",
            "eu",
            "fait",
            "faites",
            "fois",
            "font",
            "force",
            "haut",
            "hors",
            "ici",
            "il",
            "ils",
            "je",
            "juste",
            "la",
            "le",
            "les",
            "leur",
            "là",
            "ma",
            "maintenant",
            "mais",
            "mes",
            "mine",
            "moins",
            "mon",
            "mot",
            "même",
            "ni",
            "nommés",
            "notre",
            "nous",
            "nouveaux",
            "ou",
            "où",
            "par",
            "parce",
            "parole",
            "pas",
            "personnes",
            "peut",
            "peu",
            "pièce",
            "plupart",
            "pour",
            "pourquoi",
            "quand",
            "que",
            "quel",
            "quelle",
            "quelles",
            "quels",
            "qui",
            "sa",
            "sans",
            "ses",
            "seulement",
            "si",
            "sien",
            "son",
            "sont",
            "sous",
            "soyez",
            "sujet",
            "sur",
            "ta",
            "tandis",
            "tellement",
            "tels",
            "tes",
            "ton",
            "tous",
            "tout",
            "trop",
            "très",
            "tu",
            "valeur",
            "voie",
            "voient",
            "vont",
            "votre",
            "vous",
            "vu",
            "ça",
            "étaient",
            "état",
            "étions",
            "été",
            "être",
        ]
    elif language == "de":
        return [
            "aber",
            "als",
            "am",
            "an",
            "auch",
            "auf",
            "aus",
            "bei",
            "bin",
            "bis",
            "bist",
            "da",
            "dadurch",
            "daher",
            "darum",
            "das",
            "daß",
            "dass",
            "dein",
            "deine",
            "dem",
            "den",
            "der",
            "des",
            "dessen",
            "deshalb",
            "die",
            "dies",
            "dieser",
            "dieses",
            "doch",
            "dort",
            "du",
            "durch",
            "ein",
            "eine",
            "einem",
            "einen",
            "einer",
            "eines",
            "er",
            "es",
            "euer",
            "eure",
            "für",
            "hatte",
            "hatten",
            "hattest",
            "hattet",
            "hier",
            "hinter",
            "ich",
            "ihr",
            "ihre",
            "im",
            "in",
            "ist",
            "ja",
            "jede",
            "jedem",
            "jeden",
            "jeder",
            "jedes",
            "jener",
            "jenes",
            "jetzt",
            "kann",
            "kannst",
            "können",
            "könnt",
            "machen",
            "mein",
            "meine",
            "mit",
            "muß",
            "mußt",
            "musst",
            "müssen",
            "müßt",
            "nach",
            "nachdem",
            "nein",
            "nicht",
            "nun",
            "oder",
            "seid",
            "sein",
            "seine",
            "sich",
            "sie",
            "sind",
            "soll",
            "sollen",
            "sollst",
            "sollt",
            "sonst",
            "soweit",
            "sowie",
            "und",
            "unser",
            "unsere",
            "unter",
            "vom",
            "von",
            "vor",
            "wann",
            "warum",
            "was",
            "weiter",
            "weitere",
            "wenn",
            "wer",
            "werde",
            "werden",
            "werdet",
            "weshalb",
            "wie",
            "wieder",
            "wieso",
            "wir",
            "wird",
            "wirst",
            "wo",
            "woher",
            "wohin",
            "zu",
            "zum",
            "zur",
            "über",
        ]
    elif language == "es":
        return [
            "un",
            "una",
            "unas",
            "unos",
            "uno",
            "sobre",
            "todo",
            "también",
            "tras",
            "otro",
            "algún",
            "alguno",
            "alguna",
            "algunos",
            "algunas",
            "ser",
            "es",
            "soy",
            "eres",
            "somos",
            "sois",
            "estoy",
            "esta",
            "estamos",
            "estais",
            "estan",
            "como",
            "en",
            "para",
            "atras",
            "porque",
            "por",
            "qué",
            "estado",
            "estaba",
            "ante",
            "antes",
            "siendo",
            "ambos",
            "pero",
            "por",
            "poder",
            "puede",
            "puedo",
            "podemos",
            "podeis",
            "pueden",
            "fui",
            "fue",
            "fuimos",
            "fueron",
            "hacer",
            "hago",
            "hace",
            "hacemos",
            "haceis",
            "hacen",
            "cada",
            "fin",
            "incluso",
            "primero",
            "desde",
            "conseguir",
            "consigo",
            "consigue",
            "consigues",
            "conseguimos",
            "consiguen",
            "ir",
            "voy",
            "va",
            "vamos",
            "vais",
            "van",
            "vaya",
            "gueno",
            "ha",
            "tener",
            "tengo",
            "tiene",
            "tenemos",
            "teneis",
            "tienen",
            "el",
            "la",
            "lo",
            "las",
            "los",
            "su",
            "aqui",
            "mio",
            "tuyo",
            "ellos",
            "ellas",
            "nos",
            "nosotros",
            "vosotros",
            "vosotras",
            "si",
            "dentro",
            "solo",
            "solamente",
            "saber",
            "sabes",
            "sabe",
            "sabemos",
            "sabeis",
            "saben",
            "ultimo",
            "largo",
            "bastante",
            "haces",
            "muchos",
            "aquellos",
            "aquellas",
            "sus",
            "entonces",
            "tiempo",
            "verdad",
            "verdadero",
            "verdadera",
            "cierto",
            "ciertos",
            "cierta",
            "ciertas",
            "intentar",
            "intento",
            "intenta",
            "intentas",
            "intentamos",
            "intentais",
            "intentan",
            "dos",
            "bajo",
            "arriba",
            "encima",
            "usar",
            "uso",
            "usas",
            "usa",
            "usamos",
            "usais",
            "usan",
            "emplear",
            "empleo",
            "empleas",
            "emplean",
            "ampleamos",
            "empleais",
            "valor",
            "muy",
            "era",
            "eras",
            "eramos",
            "eran",
            "modo",
            "bien",
            "cual",
            "cuando",
            "donde",
            "mientras",
            "quien",
            "con",
            "entre",
            "sin",
            "trabajo",
            "trabajar",
            "trabajas",
            "trabaja",
            "trabajamos",
            "trabajais",
            "trabajan",
            "podria",
            "podrias",
            "podriamos",
            "podrian",
            "podriais",
            "yo",
            "aquel",
        ]
    else:
        return []
