import enum
from typing import List, Optional

from pydantic import BaseModel

PACKAGE_NAME = "types"


# ENUMERATIONS

class TokenPosTag(enum.Enum):
    UNKNOWN = 'UNKNOWN'
    NOUN = 'NOUN'
    ADJECTIVE_FULL = 'ADJECTIVE_FULL'
    ADJECTIVE_SHORT = 'ADJECTIVE_SHORT'
    COMPARATIVE = 'COMPARATIVE'
    VERB = 'VERB'
    INFINITIVE = 'INFINITIVE'
    PARTICLE_FULL = 'PARTICLE_FULL'
    PARTICLE_SHORT = 'PARTICLE_SHORT'
    GERUND = 'GERUND'
    NUMERICAL = 'NUMERICAL'
    ADVERB = 'ADVERB'
    NOUN_PRONOUN = 'NOUN_PRONOUN'
    PREDICATIVE = 'PREDICATIVE'
    PREPOSITION = 'PREPOSITION'
    CONJUNCTION = 'CONJUNCTION'
    PARTICLE = 'PARTICLE'
    INTERJECTION = 'INTERJECTION'
    PUNCTUATION = 'PUNCTUATION'


class TenseType(enum.Enum):
    UNKNOWN = 'UNKNOWN'
    PAST = 'PAST'
    PRESENT = 'PRESENT'
    FUTURE = 'FUTURE'


class CaseType(enum.Enum):
    UNKNOWN = 'UNKNOWN'
    NOMINATIVE = 'NOMINATIVE'
    GENITIVE = 'GENITIVE'
    DATIVE = 'DATIVE'
    ACCUSATIVE = 'ACCUSATIVE'
    INSTRUMENTAL = 'INSTRUMENTAL'
    PREPOSITIONAL = 'PREPOSITIONAL'
    VOCATION = 'VOCATION'
    GENITIVE_2 = 'GENITIVE_2'
    ACCUSATIVE_2 = 'ACCUSATIVE_2'
    PREPOSITIONAL_2 = 'PREPOSITIONAL_2'


class GenderType(enum.Enum):
    UNKNOWN = 'UNKNOWN'
    MASCULINE = 'MASCULINE'
    FEMININE = 'FEMININE'
    NEUTER = 'NEUTER'


class NumberType(enum.Enum):
    UNKNOWN = 'UNKNOWN'
    SINGULAR = 'SINGULAR'
    PLURAL = 'PLURAL'


# This type is not in use in tasks right now, consider to use it in the future
class LanguageType(enum.Enum):
    UNKNOWN = 'UNKNOWN'
    AFAR = 'AFAR'
    ABKHAZIAN = 'ABKHAZIAN'
    AVESTAN = 'AVESTAN'
    AFRIKAANS = 'AFRIKAANS'
    AKAN = 'AKAN'
    AMHARIC = 'AMHARIC'
    ARAGONESE = 'ARAGONESE'
    ARABIC = 'ARABIC'
    ASSAMESE = 'ASSAMESE'
    AVARIC = 'AVARIC'
    AYMARA = 'AYMARA'
    AZERBAIJANI = 'AZERBAIJANI'
    BASHKIR = 'BASHKIR'
    BELARUSIAN = 'BELARUSIAN'
    BULGARIAN = 'BULGARIAN'
    BIHARI_LANGUAGES = 'BIHARI_LANGUAGES'
    BISLAMA = 'BISLAMA'
    BAMBARA = 'BAMBARA'
    BENGALI = 'BENGALI'
    TIBETAN = 'TIBETAN'
    BRETON = 'BRETON'
    BOSNIAN = 'BOSNIAN'
    CATALAN = 'CATALAN'
    CHECHEN = 'CHECHEN'
    CHAMORRO = 'CHAMORRO'
    CORSICAN = 'CORSICAN'
    CREE = 'CREE'
    CZECH = 'CZECH'
    CHURCH_SLAVIC = 'CHURCH_SLAVIC'
    CHUVASH = 'CHUVASH'
    WELSH = 'WELSH'
    DANISH = 'DANISH'
    GERMAN = 'GERMAN'
    DIVEHI = 'DIVEHI'
    DZONGKHA = 'DZONGKHA'
    EWE = 'EWE'
    GREEK_MODERN = 'GREEK_MODERN'
    ENGLISH = 'ENGLISH'
    ESPERANTO = 'ESPERANTO'
    SPANISH = 'SPANISH'
    ESTONIAN = 'ESTONIAN'
    BASQUE = 'BASQUE'
    PERSIAN = 'PERSIAN'
    FULAH = 'FULAH'
    FINNISH = 'FINNISH'
    FIJIAN = 'FIJIAN'
    FAROESE = 'FAROESE'
    FRENCH = 'FRENCH'
    WESTERN_FRISIAN = 'WESTERN_FRISIAN'
    IRISH = 'IRISH'
    GAELIC = 'GAELIC'
    GALICIAN = 'GALICIAN'
    GUARANI = 'GUARANI'
    GUJARATI = 'GUJARATI'
    MANX = 'MANX'
    HAUSA = 'HAUSA'
    HEBREW = 'HEBREW'
    HINDI = 'HINDI'
    HIRI_MOTU = 'HIRI_MOTU'
    CROATIAN = 'CROATIAN'
    HAITIAN = 'HAITIAN'
    HUNGARIAN = 'HUNGARIAN'
    ARMENIAN = 'ARMENIAN'
    HERERO = 'HERERO'
    INDONESIAN = 'INDONESIAN'
    INTERLINGUE = 'INTERLINGUE'
    IGBO = 'IGBO'
    SICHUAN_YI = 'SICHUAN_YI'
    INUPIAQ = 'INUPIAQ'
    IDO = 'IDO'
    ICELANDIC = 'ICELANDIC'
    ITALIAN = 'ITALIAN'
    INUKTITUT = 'INUKTITUT'
    JAPANESE = 'JAPANESE'
    JAVANESE = 'JAVANESE'
    GEORGIAN = 'GEORGIAN'
    KONGO = 'KONGO'
    KIKUYU = 'KIKUYU'
    KUANYAMA = 'KUANYAMA'
    KAZAKH = 'KAZAKH'
    KALAALLISUT = 'KALAALLISUT'
    CENTRAL_KHMER = 'CENTRAL_KHMER'
    KANNADA = 'KANNADA'
    KOREAN = 'KOREAN'
    KANURI = 'KANURI'
    KASHMIRI = 'KASHMIRI'
    KURDISH = 'KURDISH'
    KOMI = 'KOMI'
    CORNISH = 'CORNISH'
    KIRGHIZ = 'KIRGHIZ'
    LATIN = 'LATIN'
    LUXEMBOURGISH = 'LUXEMBOURGISH'
    GANDA = 'GANDA'
    LIMBURGAN = 'LIMBURGAN'
    LINGALA = 'LINGALA'
    LAO = 'LAO'
    LITHUANIAN = 'LITHUANIAN'
    LUBA_KATANGA = 'LUBA_KATANGA'
    LATVIAN = 'LATVIAN'
    MALAGASY = 'MALAGASY'
    MARSHALLESE = 'MARSHALLESE'
    MAORI = 'MAORI'
    MACEDONIAN = 'MACEDONIAN'
    MALAYALAM = 'MALAYALAM'
    MONGOLIAN = 'MONGOLIAN'
    MARATHI = 'MARATHI'
    MALAY = 'MALAY'
    MALTESE = 'MALTESE'
    BURMESE = 'BURMESE'
    NAURU = 'NAURU'
    NDEBELE_NORTH = 'NDEBELE_NORTH'
    NEPALI = 'NEPALI'
    NDONGA = 'NDONGA'
    DUTCH = 'DUTCH'
    NORWEGIAN_NYNORSK = 'NORWEGIAN_NYNORSK'
    NORWEGIAN = 'NORWEGIAN'
    NDEBELE_SOUTH = 'NDEBELE_SOUTH'
    NAVAJO = 'NAVAJO'
    CHICHEWA = 'CHICHEWA'
    OCCITAN = 'OCCITAN'
    OJIBWA = 'OJIBWA'
    OROMO = 'OROMO'
    ORIYA = 'ORIYA'
    OSSETIAN = 'OSSETIAN'
    PANJABI = 'PANJABI'
    PALI = 'PALI'
    POLISH = 'POLISH'
    PUSHTO = 'PUSHTO'
    PORTUGUESE = 'PORTUGUESE'
    QUECHUA = 'QUECHUA'
    ROMANSH = 'ROMANSH'
    RUNDI = 'RUNDI'
    ROMANIAN = 'ROMANIAN'
    RUSSIAN = 'RUSSIAN'
    KINYARWANDA = 'KINYARWANDA'
    SANSKRIT = 'SANSKRIT'
    SARDINIAN = 'SARDINIAN'
    SINDHI = 'SINDHI'
    NORTHERN_SAMI = 'NORTHERN_SAMI'
    SANGO = 'SANGO'
    SINHALA = 'SINHALA'
    SLOVAK = 'SLOVAK'
    SLOVENIAN = 'SLOVENIAN'
    SAMOAN = 'SAMOAN'
    SHONA = 'SHONA'
    SOMALI = 'SOMALI'
    ALBANIAN = 'ALBANIAN'
    SERBIAN = 'SERBIAN'
    SWATI = 'SWATI'
    SOTHO_SOUTHERN = 'SOTHO_SOUTHERN'
    SUNDANESE = 'SUNDANESE'
    SWEDISH = 'SWEDISH'
    SWAHILI = 'SWAHILI'
    TAMIL = 'TAMIL'
    TELUGU = 'TELUGU'
    TAJIK = 'TAJIK'
    THAI = 'THAI'
    TIGRINYA = 'TIGRINYA'
    TURKMEN = 'TURKMEN'
    TAGALOG = 'TAGALOG'
    TSWANA = 'TSWANA'
    TONGA = 'TONGA'
    TURKISH = 'TURKISH'
    TSONGA = 'TSONGA'
    TATAR = 'TATAR'
    TWI = 'TWI'
    TAHITIAN = 'TAHITIAN'
    UIGHUR = 'UIGHUR'
    UKRAINIAN = 'UKRAINIAN'
    URDU = 'URDU'
    UZBEK = 'UZBEK'
    VENDA = 'VENDA'
    VIETNAMESE = 'VIETNAMESE'
    WALLOON = 'WALLOON'
    WOLOF = 'WOLOF'
    XHOSA = 'XHOSA'
    YIDDISH = 'YIDDISH'
    YORUBA = 'YORUBA'
    ZHUANG = 'ZHUANG'
    CHINESE = 'CHINESE'
    ZULU = 'ZULU'


class EntityType(enum.Enum):
    UNKNOWN = 'UNKNOWN'
    PERSON = 'PERSON'
    TOPONYM = 'TOPONYM'
    LOCATION = 'LOCATION'
    ORGANIZATION = 'ORGANIZATION'
    SURNAME = 'SURNAME'
    FIRST_NAME = 'FIRST_NAME'
    PATRNAME = 'PATRNAME'
    OBSCENE = 'OBSCENE'
    LATIN_CHARS = 'LATIN_CHARS'
    INTEGER_NUMBER = 'INTEGER_NUMBER'
    ORDINAL_NUMBER = 'ORDINAL_NUMBER'
    ROMNUMBER = 'ROMNUMBER'
    CARDINAL_NUMBER = 'CARDINAL_NUMBER'
    AMOUNT_OF_MONEY = 'AMOUNT_OF_MONEY'
    QUANTITY = 'QUANTITY'
    ABBREVIATION = 'ABBREVIATION'
    DISTANCE = 'DISTANCE'
    TEMPERATURE = 'TEMPERATURE'
    VOLUME = 'VOLUME'
    TIME = 'TIME'
    DATE = 'DATE'
    DATETIME = 'DATETIME'
    TIME_DURATION = 'TIME_DURATION'
    TIME_INTERVAL = 'TIME_INTERVAL'
    PHONE_NUMBER = 'PHONE_NUMBER'
    EMAIL = 'EMAIL'
    URL = 'URL'
    EVENT = 'EVENT'
    BUILDING = 'BUILDING'
    LANGUAGE = 'LANGUAGE'
    LAW = 'LAW'
    COMMUNITY = 'COMMUNITY'
    PERCENT = 'PERCENT'
    PRODUCT = 'PRODUCT'
    WORK_OF_ART = 'WORK_OF_ART'


class SourceType(enum.Enum):
    UNKNOWN = 'UNKNOWN'
    DUCKLING = 'DUCKLING'
    MYSTEM = 'MYSTEM'
    PYMORPHY = 'PYMORPHY'
    MLPS = 'MLPS'
    SPACY = 'SPACY'
    SLOVNET = 'SLOVNET'
    DEEPPAVLOV = 'DEEPPAVLOV'


# COMPONENTS

class Span(BaseModel):
    start_index: int
    end_index: int


class SpanWithConfidence(Span):
    confidence: float


class AlignedSpans(BaseModel):
    original_spans: List[Span]
    new_spans: List[Span]


class Token(BaseModel):
    value: str
    span: Span


class Tokens(BaseModel):
    tokens: List[Token]


class Item(BaseModel):
    value: str


class Items(BaseModel):
    items: List[Item]


class ScoredItems(Items):
    scores: List[float]


class EmbeddingVector(BaseModel):
    vector: List[float]


class ScoredLanguages(BaseModel):
    languages: List[str]
    scores: List[float]


class ScoredTextInfo(BaseModel):
    text: str
    score: float
    positive_labels: List[Item]
    negative_labels: List[Item]


class MetricClassifierScoredItems(ScoredItems):
    info: List[ScoredTextInfo]


class RawInformationValue(BaseModel):
    value: str


class NamedEntity(RawInformationValue):
    entity_type: str
    span: Span
    entity: str
    source_type: str


class NamedEntities(BaseModel):
    entities: List[NamedEntity]


class Texts(BaseModel):
    values: List[str]


class ExtractedText(SpanWithConfidence):
    text: str


class ExtractedTexts(BaseModel):
    texts: List[ExtractedText]


class ExtractedTextsList(BaseModel):
    extracted_texts_list: List[ExtractedTexts]


class CaseTag(BaseModel):
    case: Optional[CaseType]


class GenderTag(BaseModel):
    gender: Optional[GenderType]


class NumberTag(BaseModel):
    number: Optional[NumberType]


class PosTag(BaseModel):
    pos_tag: TokenPosTag


class TenseTag(BaseModel):
    tense: Optional[TenseType]


class InflectorTag(CaseTag, GenderTag, NumberTag, TenseTag):
    pass


class TokenWithRawInfo(RawInformationValue):
    token: Token


class TokensWithRawInfo(BaseModel):
    tokens: List[TokenWithRawInfo]
    source: str


class CorrectedInstance(BaseModel):
    value: str
    variants: List[str]
    span: Span


class CorrectedInstances(BaseModel):
    instances: List[CorrectedInstance]
    alignment: AlignedSpans


class ScoredSeq2SeqTexts(Texts):
    similarity_scores: Optional[List[float]]
    perplexity_scores: Optional[List[float]]


# COLLECTIONS

class TextsCollection(BaseModel):
    texts: List[str]


class EmbeddedTextsCollection(BaseModel):
    embedded_texts: List[EmbeddingVector]


class TextsListCollection(BaseModel):
    texts_list: List[Texts]


class FlagsCollection(BaseModel):
    flags: List[bool]


class ItemsCollection(BaseModel):
    items_list: List[Items]


class DoubledItemsCollection(ItemsCollection):
    extra_items_list: List[Items]


class TextsWithQueriesListCollection(TextsCollection):
    queries_list: List[Texts]


class InflectorTextsCollection(TextsCollection):
    tags: List[InflectorTag]


class ConformerTextsCollection(TextsCollection):
    numbers: List[int]


class ScoredItemsCollection(ItemsCollection):
    items_list: List[ScoredItems]


class TextsWithScoredItemsCollection(ScoredItemsCollection, TextsCollection):
    pass


class ScoredItemsWithInfoCollection(ScoredItemsCollection):
    items_list: List[MetricClassifierScoredItems]


class ScoredLanguagesCollection(BaseModel):
    scored_languages_list: List[ScoredLanguages]


class TokenizedTextsCollection(BaseModel):
    tokens_list: List[Tokens]


class CorrectedInstancesCollection(BaseModel):
    corrected_texts: List[str]
    corrected_instances_list: List[CorrectedInstances]


class NamedEntitiesCollection(BaseModel):
    entities_list: List[NamedEntities]


class TokensWithRawInfoCollection(BaseModel):
    tokens_list: List[TokensWithRawInfo]


class ExtractedTextsCollection(BaseModel):
    texts_list: List[ExtractedTextsList]


class ScoredSeq2SeqTextsListCollection(BaseModel):
    texts_list: List[ScoredSeq2SeqTexts]


# TEST COMPONENTS

class SpanTest(Span):
    middle_index: int


class TokenTest(Token):
    span: SpanTest
    info: str
    source: str


class TokensTest(Tokens):
    tokens: List[TokenTest]
    value: str


class TokensErrorTest(TokensTest):
    value: List[str]


# TEST COLLECTIONS

class InflectorConformerTextsCollectionTest(ConformerTextsCollection, InflectorTextsCollection):
    dummy: str = ''
    dummy_base: ScoredItems = ''


class TokenizedTextsCollectionTest(TokenizedTextsCollection):
    tokens_list: List[TokensTest]
    some_nested_field: List[TokensTest]
    some_complex_field: Tokens
    some_simple_field: str = ''


class TokenizedTextsCollectionWithErrorTest(TokenizedTextsCollection):
    tokens_list: int = 0
