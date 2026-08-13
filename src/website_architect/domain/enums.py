from enum import Enum


class SiteType(str, Enum):
    LANDING_PAGE = "landing_page"
    SAAS = "saas"
    AGENCY = "agency"
    PORTFOLIO = "portfolio"
    ECOMMERCE = "ecommerce"
    TRAVEL = "travel"
    WELLNESS = "wellness"
    FINTECH = "fintech"
    TECHNOLOGY = "technology"
    FASHION = "fashion"


class SiteMode(str, Enum):
    SINGLE_PAGE = "single_page"
    MULTI_PAGE = "multi_page"


class Topology(str, Enum):
    SEQUENTIAL = "sequential"
    HIERARCHICAL = "hierarchical"
    MATRIX = "matrix"


class NodeType(str, Enum):
    PAGE = "page"
    TEMPLATE = "template"
    COLLECTION = "collection"
    SECTION = "section"


class LinkType(str, Enum):
    NAVIGATION = "navigation"
    CTA = "cta"