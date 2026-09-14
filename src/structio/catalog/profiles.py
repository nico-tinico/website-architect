from structio.domain.enums import (
    LinkType,
    NodeType,
    SiteType,
    Topology,
)
from structio.domain.nodes import PageDefinition

from .definitions import LinkRule, SiteProfile, TemplateDefinition, profile


# ---------------------------------------------------------------------------
# Definition helpers
# ---------------------------------------------------------------------------


def section(
    name: str,
    *,
    purpose: str,
    required: bool = True,
) -> PageDefinition:
    return PageDefinition(
        name=name,
        node_type=NodeType.SECTION,
        required=required,
        repeatable=False,
        purpose=purpose,
        children=(),
    )


def page(
    name: str,
    *,
    purpose: str,
    required: bool = True,
    children: tuple[PageDefinition, ...] = (),
) -> PageDefinition:
    return PageDefinition(
        name=name,
        node_type=NodeType.PAGE,
        required=required,
        repeatable=False,
        purpose=purpose,
        children=children,
    )


def collection(
    name: str,
    *,
    purpose: str,
    item_template: str,
    required: bool = True,
    children: tuple[PageDefinition, ...] = (),
) -> PageDefinition:
    return PageDefinition(
        name=name,
        node_type=NodeType.COLLECTION,
        required=required,
        repeatable=False,
        purpose=purpose,
        children=children,
        item_template=item_template,
    )


def template(
    name: str,
    *,
    purpose: str,
    required: bool = True,
) -> TemplateDefinition:
    return TemplateDefinition(
        name=name,
        required=required,
        purpose=purpose,
    )


def entry_point(
    name: str,
    *,
    purpose: str,
    target_template: str,
    required: bool = True,
) -> PageDefinition:
    return PageDefinition(
        name=name,
        node_type=NodeType.ENTRY_POINT,
        required=required,
        repeatable=False,
        purpose=purpose,
        children=(),
        target_template=target_template,
    )


# ---------------------------------------------------------------------------
# Landing Page
# ---------------------------------------------------------------------------


LANDING_PAGE = profile(
    site_type=SiteType.LANDING_PAGE,
    default_topology=Topology.SEQUENTIAL,
    single_page=(
        section(
            "Hero",
            purpose=(
                "Introduce the offering, establish the main value proposition, "
                "and direct visitors toward the primary action."
            ),
        ),
        section(
            "Problem",
            purpose=(
                "Explain the problem, need, or opportunity addressed by the offering."
            ),
        ),
        section(
            "Solution",
            purpose=(
                "Explain how the offering solves the problem and communicates "
                "its core value."
            ),
        ),
        section(
            "Features",
            purpose=(
                "Present the main capabilities, characteristics, or benefits "
                "of the offering."
            ),
        ),
        section(
            "Social Proof",
            purpose=(
                "Build credibility through testimonials, customers, metrics, "
                "logos, or other forms of evidence."
            ),
        ),
        section(
            "FAQ",
            required=False,
            purpose=(
                "Resolve common questions or objections that may prevent "
                "visitors from taking action."
            ),
        ),
        section(
            "CTA",
            purpose=(
                "Provide the primary conversion opportunity and guide visitors "
                "toward the desired action."
            ),
        ),
    ),
    multi_page=(
        page(
            "Home",
            purpose="Introduce the offering and communicate its primary value proposition.",
        ),
        page(
            "Features",
            purpose="Present the main capabilities and benefits of the offering.",
        ),
        page(
            "About",
            required=False,
            purpose="Explain the company, project, or organization behind the offering.",
        ),
        page(
            "FAQ",
            required=False,
            purpose="Answer common questions and address visitor objections.",
        ),
        page(
            "Contact",
            purpose="Provide a direct way for visitors to contact the organization.",
        ),
    ),
    single_page_links=(
        LinkRule("Hero", "Problem", LinkType.NAVIGATION),
        LinkRule("Problem", "Solution", LinkType.NAVIGATION),
        LinkRule("Solution", "Features", LinkType.NAVIGATION),
        LinkRule("Features", "Social Proof", LinkType.NAVIGATION),
        LinkRule("Social Proof", "FAQ", LinkType.NAVIGATION),
        LinkRule("FAQ", "CTA", LinkType.NAVIGATION),
        LinkRule("Hero", "CTA", LinkType.CTA),
    ),
    multi_page_links=(
        LinkRule("Home", "Features", LinkType.NAVIGATION),
        LinkRule("Home", "About", LinkType.NAVIGATION),
        LinkRule("Home", "FAQ", LinkType.NAVIGATION),
        LinkRule("Home", "Contact", LinkType.NAVIGATION),
        LinkRule("Features", "Contact", LinkType.CTA),
        LinkRule("About", "Contact", LinkType.CTA),
    ),
)


# ---------------------------------------------------------------------------
# SaaS
# ---------------------------------------------------------------------------


SAAS_TEMPLATES = (
    template(
        "Article",
        purpose=(
            "Present an individual resource article, guide, or editorial "
            "piece published by the SaaS company."
        ),
    ),
)


SAAS = profile(
    site_type=SiteType.SAAS,
    default_topology=Topology.HIERARCHICAL,
    single_page=(
        section(
            "Hero",
            purpose=(
                "Communicate the SaaS product's value proposition and drive "
                "visitors toward the primary conversion action."
            ),
        ),
        section(
            "Product",
            purpose=(
                "Explain the product and how its core capabilities solve "
                "customer problems."
            ),
        ),
        section(
            "Features",
            purpose=(
                "Present the product's main features and functional capabilities."
            ),
        ),
        section(
            "Solutions",
            required=False,
            purpose=(
                "Explain how the product addresses the needs of different "
                "customer segments or use cases."
            ),
        ),
        section(
            "Pricing",
            purpose=(
                "Communicate pricing plans and help users select the appropriate "
                "commercial offering."
            ),
        ),
        section(
            "Social Proof",
            required=False,
            purpose=(
                "Build trust through customer evidence, testimonials, logos, "
                "or measurable outcomes."
            ),
        ),
        section(
            "CTA",
            purpose=(
                "Convert visitors into trial users, customers, or qualified leads."
            ),
        ),
    ),
    multi_page=(
        page(
            "Home",
            purpose="Introduce the SaaS product and communicate its core value proposition.",
        ),
        page(
            "Product",
            purpose="Provide a detailed explanation of the SaaS product and its capabilities.",
        ),
        page(
            "Features",
            purpose="Present the main features and functional capabilities of the product.",
        ),
        page(
            "Solutions",
            required=False,
            purpose="Present solutions for different customer segments or use cases.",
        ),
        page(
            "Pricing",
            purpose="Present pricing plans and commercial options.",
        ),
        page(
            "Resources",
            required=False,
            purpose="Provide educational, editorial, and product-related resources.",
            children=(
                page(
                    "Blog",
                    required=False,
                    purpose="Publish company and industry articles.",
                ),
                page(
                    "Guides",
                    required=False,
                    purpose="Provide educational guides and practical resources.",
                ),
            ),
        ),
        page(
            "Company",
            required=False,
            purpose="Provide information about the company behind the SaaS product.",
            children=(
                page(
                    "About",
                    purpose="Explain the company, mission, and organization.",
                ),
                page(
                    "Careers",
                    required=False,
                    purpose="Present open roles and employment opportunities.",
                ),
                page(
                    "Contact",
                    required=False,
                    purpose="Provide a way to contact the company.",
                ),
            ),
        ),
        page(
            "Login",
            purpose="Allow existing users to access their SaaS account.",
        ),
        page(
            "Signup",
            purpose="Allow new users to create an account or start using the product.",
        ),
    ),
    single_page_links=(
        LinkRule("Hero", "Product", LinkType.NAVIGATION),
        LinkRule("Product", "Features", LinkType.NAVIGATION),
        LinkRule("Features", "Solutions", LinkType.NAVIGATION),
        LinkRule("Solutions", "Pricing", LinkType.NAVIGATION),
        LinkRule("Pricing", "Social Proof", LinkType.NAVIGATION),
        LinkRule("Social Proof", "CTA", LinkType.NAVIGATION),
        LinkRule("Hero", "CTA", LinkType.CTA),
    ),
    multi_page_links=(
        LinkRule("Home", "Product", LinkType.NAVIGATION),
        LinkRule("Home", "Features", LinkType.NAVIGATION),
        LinkRule("Home", "Solutions", LinkType.NAVIGATION),
        LinkRule("Home", "Pricing", LinkType.NAVIGATION),
        LinkRule("Home", "Resources", LinkType.NAVIGATION),
        LinkRule("Home", "Company", LinkType.NAVIGATION),
        LinkRule("Home", "Login", LinkType.NAVIGATION),
        LinkRule("Product", "Signup", LinkType.CTA),
        LinkRule("Pricing", "Signup", LinkType.CTA),
        LinkRule("Solutions", "Signup", LinkType.CTA),
    ),
    templates=SAAS_TEMPLATES,
)


# ---------------------------------------------------------------------------
# Agency
# ---------------------------------------------------------------------------


AGENCY_TEMPLATES = (
    template(
        "Service",
        purpose=(
            "Present an individual agency service, its capabilities, value, "
            "and relevance to client needs."
        ),
    ),
    template(
        "Case Study",
        purpose=(
            "Present an individual client project, including its context, "
            "approach, solution, and outcomes."
        ),
    ),
)


AGENCY = profile(
    site_type=SiteType.AGENCY,
    default_topology=Topology.MATRIX,
    single_page=(
        section(
            "Hero",
            purpose="Introduce the agency and communicate its core positioning and value.",
        ),
        section(
            "Services",
            purpose="Present the agency's primary services and capabilities.",
        ),
        section(
            "Work",
            purpose="Showcase selected projects and demonstrate the agency's capabilities.",
        ),
        section(
            "Process",
            required=False,
            purpose="Explain how the agency approaches projects and collaborates with clients.",
        ),
        section(
            "About",
            purpose="Present the agency, its team, values, and positioning.",
        ),
        section(
            "Testimonials",
            required=False,
            purpose="Provide client feedback and social proof.",
        ),
        section(
            "CTA",
            purpose="Encourage visitors to start a conversation or project.",
        ),
    ),
    multi_page=(
        page(
            "Home",
            purpose="Introduce the agency and communicate its positioning.",
        ),
        page(
            "Services",
            purpose="Present the agency's service offering.",
            children=(
                collection(
                    "Service",
                    purpose="Organize the agency's individual service offerings.",
                    item_template="Service",
                ),
            ),
        ),
        entry_point(
            "Service",
            purpose="Provide direct access to individual service pages.",
            target_template="Service",
        ),
        page(
            "Work",
            purpose="Showcase the agency's portfolio of client work.",
            children=(
                collection(
                    "Case Studies",
                    purpose="Organize individual client projects and case studies.",
                    item_template="Case Study",
                ),
            ),
        ),
        entry_point(
            "Case Study",
            purpose="Provide direct access to individual case study pages.",
            target_template="Case Study",
        ),
        page(
            "About",
            purpose="Present the agency, its team, values, and positioning.",
        ),
        page(
            "Contact",
            purpose="Provide a way for prospective clients to contact the agency.",
        ),
    ),
    single_page_links=(
        LinkRule("Hero", "Services", LinkType.NAVIGATION),
        LinkRule("Services", "Work", LinkType.NAVIGATION),
        LinkRule("Work", "Process", LinkType.NAVIGATION),
        LinkRule("Process", "About", LinkType.NAVIGATION),
        LinkRule("About", "Testimonials", LinkType.NAVIGATION),
        LinkRule("Testimonials", "CTA", LinkType.NAVIGATION),
        LinkRule("Hero", "CTA", LinkType.CTA),
    ),
    multi_page_links=(
        LinkRule("Home", "Services", LinkType.NAVIGATION),
        LinkRule("Home", "Work", LinkType.NAVIGATION),
        LinkRule("Home", "About", LinkType.NAVIGATION),
        LinkRule("Home", "Contact", LinkType.NAVIGATION),
        LinkRule("Services", "Service", LinkType.NAVIGATION),
        LinkRule("Work", "Case Study", LinkType.NAVIGATION),
        LinkRule("Service", "Contact", LinkType.CTA),
        LinkRule("Case Study", "Contact", LinkType.CTA),
    ),
    templates=AGENCY_TEMPLATES,
)


# ---------------------------------------------------------------------------
# Portfolio
# ---------------------------------------------------------------------------


PORTFOLIO_TEMPLATES = (
    template(
        "Project",
        purpose=(
            "Present an individual portfolio project, including its context, "
            "role, process, and outcome."
        ),
    ),
)


PORTFOLIO = profile(
    site_type=SiteType.PORTFOLIO,
    default_topology=Topology.SEQUENTIAL,
    single_page=(
        section(
            "Hero",
            purpose="Introduce the portfolio owner and establish their professional positioning.",
        ),
        section(
            "About",
            purpose="Present the portfolio owner, background, skills, and professional identity.",
        ),
        section(
            "Selected Work",
            purpose="Showcase representative projects and demonstrate capabilities.",
        ),
        section(
            "Skills",
            required=False,
            purpose="Present the main skills, disciplines, or technologies of the portfolio owner.",
        ),
        section(
            "Experience",
            required=False,
            purpose="Present relevant professional experience and career history.",
        ),
        section(
            "Contact",
            purpose="Provide a way for visitors to start a professional conversation.",
        ),
    ),
    multi_page=(
        page(
            "Home",
            purpose="Introduce the portfolio owner and highlight selected work.",
        ),
        page(
            "Work",
            purpose="Present the portfolio owner's projects.",
            children=(
                collection(
                    "Projects",
                    purpose="Organize the portfolio's individual projects.",
                    item_template="Project",
                ),
            ),
        ),
        entry_point(
            "Project",
            purpose="Provide direct access to individual portfolio project pages.",
            target_template="Project",
        ),
        page(
            "About",
            purpose="Present the portfolio owner's background, identity, and professional positioning.",
        ),
        page(
            "Contact",
            purpose="Provide a way to contact the portfolio owner.",
        ),
    ),
    single_page_links=(
        LinkRule("Hero", "About", LinkType.NAVIGATION),
        LinkRule("About", "Selected Work", LinkType.NAVIGATION),
        LinkRule("Selected Work", "Skills", LinkType.NAVIGATION),
        LinkRule("Skills", "Experience", LinkType.NAVIGATION),
        LinkRule("Experience", "Contact", LinkType.NAVIGATION),
        LinkRule("Hero", "Contact", LinkType.CTA),
    ),
    multi_page_links=(
        LinkRule("Home", "Work", LinkType.NAVIGATION),
        LinkRule("Home", "About", LinkType.NAVIGATION),
        LinkRule("Home", "Contact", LinkType.NAVIGATION),
        LinkRule("Work", "Project", LinkType.NAVIGATION),
        LinkRule("Project", "Contact", LinkType.CTA),
    ),
    templates=PORTFOLIO_TEMPLATES,
)


# ---------------------------------------------------------------------------
# Ecommerce
# ---------------------------------------------------------------------------


ECOMMERCE_TEMPLATES = (
    template(
        "Product",
        purpose=(
            "Present an individual product and support product evaluation "
            "and purchase."
        ),
    ),
    template(
        "Collection",
        purpose=(
            "Present a curated group of products around a common theme "
            "or merchandising concept."
        ),
    ),
)


ECOMMERCE = profile(
    site_type=SiteType.ECOMMERCE,
    default_topology=Topology.MATRIX,
    single_page=(
        section(
            "Hero",
            purpose=(
                "Introduce the store, establish the brand proposition, "
                "and direct users toward product discovery."
            ),
        ),
        section(
            "Featured Products",
            purpose=(
                "Highlight selected products that the store wants users "
                "to discover or consider."
            ),
        ),
        section(
            "Categories",
            purpose=(
                "Help users discover products through the store's main "
                "product categories."
            ),
        ),
        section(
            "Collections",
            required=False,
            purpose=(
                "Present curated groups of products organized around "
                "themes, campaigns, or merchandising concepts."
            ),
        ),
        section(
            "Best Sellers",
            required=False,
            purpose=(
                "Highlight products with strong demand or popularity "
                "to guide product discovery."
            ),
        ),
        section(
            "New Arrivals",
            required=False,
            purpose=(
                "Showcase recently introduced products and encourage "
                "users to explore new inventory."
            ),
        ),
        section(
            "Offers",
            required=False,
            purpose=(
                "Communicate promotions, discounts, or commercial "
                "opportunities available to shoppers."
            ),
        ),
        section(
            "Reviews",
            required=False,
            purpose=(
                "Provide customer feedback and social proof to support "
                "product evaluation and purchasing decisions."
            ),
        ),
        section(
            "CTA",
            purpose=(
                "Direct users toward shopping, product discovery, "
                "or another primary commercial action."
            ),
        ),
    ),
    multi_page=(
        page(
            "Shop",
            purpose=(
                "Provide the main product discovery and browsing "
                "experience for the store."
            ),
            children=(
                collection(
                    "Category",
                    purpose=(
                        "Organize products into meaningful categories "
                        "for browsing and discovery."
                    ),
                    item_template="Product",
                ),
                collection(
                    "Collections",
                    required=False,
                    purpose=(
                        "Organize curated groups of products around "
                        "themes, campaigns, or merchandising strategies."
                    ),
                    item_template="Collection",
                ),
                page(
                    "Search",
                    required=False,
                    purpose=(
                        "Allow users to search, filter, and discover "
                        "products across the catalog."
                    ),
                ),
            ),
        ),
        entry_point(
            "Product",
            purpose="Provide direct access to individual product pages.",
            target_template="Product",
        ),
        page(
            "Wishlist",
            required=False,
            purpose=(
                "Allow users to save and revisit products they are "
                "interested in purchasing."
            ),
        ),
        page(
            "Cart",
            purpose=(
                "Review selected products, quantities, prices, "
                "and prepare the order for checkout."
            ),
        ),
        page(
            "Checkout",
            purpose=(
                "Complete the purchase by collecting order, shipping, "
                "billing, and payment information."
            ),
        ),
        page(
            "Account",
            required=False,
            purpose=(
                "Provide authenticated users with access to their profile, "
                "orders, addresses, and account settings."
            ),
            children=(
                page(
                    "Profile",
                    purpose="Allow users to view and manage personal account information.",
                ),
                page(
                    "Orders",
                    purpose="Allow users to review their current and previous orders.",
                ),
                page(
                    "Addresses",
                    purpose="Allow users to manage saved shipping and billing addresses.",
                ),
            ),
        ),
        page(
            "Journal",
            required=False,
            purpose=(
                "Publish editorial content, brand stories, product "
                "inspiration, or other content supporting the shopping experience."
            ),
        ),
        page(
            "Support",
            required=False,
            purpose=(
                "Provide assistance and information for customers before, "
                "during, or after a purchase."
            ),
        ),
    ),
    single_page_links=(
        LinkRule("Hero", "Featured Products", LinkType.NAVIGATION),
        LinkRule("Featured Products", "Categories", LinkType.NAVIGATION),
        LinkRule("Categories", "Collections", LinkType.NAVIGATION),
        LinkRule("Collections", "Best Sellers", LinkType.NAVIGATION),
        LinkRule("Best Sellers", "New Arrivals", LinkType.NAVIGATION),
        LinkRule("New Arrivals", "Offers", LinkType.NAVIGATION),
        LinkRule("Offers", "Reviews", LinkType.NAVIGATION),
        LinkRule("Reviews", "CTA", LinkType.NAVIGATION),
        LinkRule("Hero", "CTA", LinkType.CTA),
    ),
    multi_page_links=(
        LinkRule("Home", "Shop", LinkType.NAVIGATION),
        LinkRule("Home", "Product", LinkType.NAVIGATION),
        LinkRule("Home", "Wishlist", LinkType.NAVIGATION),
        LinkRule("Home", "Cart", LinkType.NAVIGATION),
        LinkRule("Home", "Account", LinkType.NAVIGATION),
        LinkRule("Home", "Journal", LinkType.NAVIGATION),
        LinkRule("Shop", "Product", LinkType.NAVIGATION),
        LinkRule("Product", "Wishlist", LinkType.CTA),
        LinkRule("Product", "Cart", LinkType.CTA),
        LinkRule("Cart", "Checkout", LinkType.NAVIGATION),
        LinkRule("Checkout", "Account", LinkType.NAVIGATION),
        LinkRule("Journal", "Shop", LinkType.CTA),
    ),
    templates=ECOMMERCE_TEMPLATES,
)


# ---------------------------------------------------------------------------
# Travel
# ---------------------------------------------------------------------------


TRAVEL_TEMPLATES = (
    template(
        "Destination",
        purpose=(
            "Present an individual destination, its highlights, places, "
            "and practical travel information."
        ),
    ),
    template(
        "Experience",
        purpose=(
            "Present an individual travel experience, its details, value, "
            "and participation or booking information."
        ),
    ),
    template(
        "Itinerary",
        purpose=(
            "Present an individual travel itinerary with its sequence "
            "of destinations and activities."
        ),
    ),
)


TRAVEL = profile(
    site_type=SiteType.TRAVEL,
    default_topology=Topology.MATRIX,
    single_page=(
        section(
            "Hero",
            purpose="Introduce the travel offering and inspire destination discovery.",
        ),
        section(
            "Destinations",
            purpose="Highlight destinations and encourage visitors to explore them.",
        ),
        section(
            "Experiences",
            purpose="Present selected travel experiences and activities.",
        ),
        section(
            "Itineraries",
            required=False,
            purpose="Present curated travel itineraries and journeys.",
        ),
        section(
            "Inspiration",
            required=False,
            purpose="Provide editorial content and inspiration for travel planning.",
        ),
        section(
            "CTA",
            purpose="Guide visitors toward planning, booking, or exploring a trip.",
        ),
    ),
    multi_page=(
        page(
            "Home",
            purpose="Introduce the travel offering and inspire visitors to explore.",
        ),
        page(
            "Destinations",
            purpose="Provide access to the available destinations.",
            children=(
                collection(
                    "Destination",
                    purpose="Organize individual travel destinations.",
                    item_template="Destination",
                ),
            ),
        ),
        entry_point(
            "Destination",
            purpose="Provide direct access to individual destination pages.",
            target_template="Destination",
        ),
        page(
            "Experiences",
            purpose="Provide access to available travel experiences.",
            children=(
                collection(
                    "Experience",
                    purpose="Organize individual travel experiences and activities.",
                    item_template="Experience",
                ),
            ),
        ),
        entry_point(
            "Experience",
            purpose="Provide direct access to individual experience pages.",
            target_template="Experience",
        ),
        page(
            "Itineraries",
            required=False,
            purpose="Present curated travel itineraries.",
            children=(
                collection(
                    "Itinerary",
                    purpose="Organize individual travel itineraries.",
                    item_template="Itinerary",
                ),
            ),
        ),
        entry_point(
            "Itinerary",
            required=False,
            purpose="Provide direct access to individual itinerary pages.",
            target_template="Itinerary",
        ),
        page(
            "Journal",
            required=False,
            purpose="Publish travel stories, guides, inspiration, and editorial content.",
        ),
        page(
            "Contact",
            required=False,
            purpose="Provide a way for visitors to contact the travel organization.",
        ),
    ),
    single_page_links=(
        LinkRule("Hero", "Destinations", LinkType.NAVIGATION),
        LinkRule("Destinations", "Experiences", LinkType.NAVIGATION),
        LinkRule("Experiences", "Itineraries", LinkType.NAVIGATION),
        LinkRule("Itineraries", "Inspiration", LinkType.NAVIGATION),
        LinkRule("Inspiration", "CTA", LinkType.NAVIGATION),
        LinkRule("Hero", "CTA", LinkType.CTA),
    ),
    multi_page_links=(
        LinkRule("Home", "Destinations", LinkType.NAVIGATION),
        LinkRule("Home", "Experiences", LinkType.NAVIGATION),
        LinkRule("Home", "Itineraries", LinkType.NAVIGATION),
        LinkRule("Home", "Journal", LinkType.NAVIGATION),
        LinkRule("Destinations", "Destination", LinkType.NAVIGATION),
        LinkRule("Experiences", "Experience", LinkType.NAVIGATION),
        LinkRule("Itineraries", "Itinerary", LinkType.NAVIGATION),
        LinkRule("Destination", "Experience", LinkType.CTA),
        LinkRule("Experience", "Itinerary", LinkType.CTA),
    ),
    templates=TRAVEL_TEMPLATES,
)


# ---------------------------------------------------------------------------
# Wellness
# ---------------------------------------------------------------------------


WELLNESS_TEMPLATES = (
    template(
        "Service",
        purpose="Present an individual wellness service, its benefits, process, and participation information.",
    ),
    template(
        "Program",
        purpose="Present an individual wellness program, its structure, goals, and participation details.",
    ),
)


WELLNESS = profile(
    site_type=SiteType.WELLNESS,
    default_topology=Topology.HIERARCHICAL,
    single_page=(
        section(
            "Hero",
            purpose="Introduce the wellness offering and communicate its positioning.",
        ),
        section(
            "Services",
            purpose="Present the primary wellness services.",
        ),
        section(
            "Programs",
            required=False,
            purpose="Present structured wellness programs and journeys.",
        ),
        section(
            "Approach",
            purpose="Explain the philosophy, methodology, or approach behind the wellness offering.",
        ),
        section(
            "Testimonials",
            required=False,
            purpose="Provide customer feedback and social proof.",
        ),
        section(
            "FAQ",
            required=False,
            purpose="Answer common questions about the wellness offering.",
        ),
        section(
            "CTA",
            purpose="Guide visitors toward booking, consultation, or another primary action.",
        ),
    ),
    multi_page=(
        page(
            "Home",
            purpose="Introduce the wellness offering and communicate its positioning.",
        ),
        page(
            "Services",
            purpose="Present the available wellness services.",
            children=(
                collection(
                    "Service",
                    purpose="Organize individual wellness services.",
                    item_template="Service",
                ),
            ),
        ),
        entry_point(
            "Service",
            purpose="Provide direct access to individual wellness service pages.",
            target_template="Service",
        ),
        page(
            "Programs",
            required=False,
            purpose="Present structured wellness programs and journeys.",
            children=(
                collection(
                    "Program",
                    purpose="Organize individual wellness programs.",
                    item_template="Program",
                ),
            ),
        ),
        entry_point(
            "Program",
            required=False,
            purpose="Provide direct access to individual wellness program pages.",
            target_template="Program",
        ),
        page(
            "About",
            purpose="Explain the organization, practitioners, philosophy, and approach.",
        ),
        page(
            "Contact",
            purpose="Provide a way to contact the wellness organization.",
        ),
    ),
    single_page_links=(
        LinkRule("Hero", "Services", LinkType.NAVIGATION),
        LinkRule("Services", "Programs", LinkType.NAVIGATION),
        LinkRule("Programs", "Approach", LinkType.NAVIGATION),
        LinkRule("Approach", "Testimonials", LinkType.NAVIGATION),
        LinkRule("Testimonials", "FAQ", LinkType.NAVIGATION),
        LinkRule("FAQ", "CTA", LinkType.NAVIGATION),
        LinkRule("Hero", "CTA", LinkType.CTA),
    ),
    multi_page_links=(
        LinkRule("Home", "Services", LinkType.NAVIGATION),
        LinkRule("Home", "Programs", LinkType.NAVIGATION),
        LinkRule("Home", "About", LinkType.NAVIGATION),
        LinkRule("Home", "Contact", LinkType.NAVIGATION),
        LinkRule("Services", "Service", LinkType.NAVIGATION),
        LinkRule("Programs", "Program", LinkType.NAVIGATION),
        LinkRule("Service", "Contact", LinkType.CTA),
        LinkRule("Program", "Contact", LinkType.CTA),
    ),
    templates=WELLNESS_TEMPLATES,
)


# ---------------------------------------------------------------------------
# Fintech
# ---------------------------------------------------------------------------


FINTECH_TEMPLATES = (
    template(
        "Solution",
        purpose="Present an individual financial solution and explain how it addresses a specific customer need.",
    ),
)


FINTECH = profile(
    site_type=SiteType.FINTECH,
    default_topology=Topology.MATRIX,
    single_page=(
        section(
            "Hero",
            purpose="Communicate the fintech offering and establish trust and value.",
        ),
        section(
            "Solutions",
            purpose="Present the main financial products or solutions.",
        ),
        section(
            "How It Works",
            purpose="Explain the process and user experience of the financial service.",
        ),
        section(
            "Security",
            purpose="Explain security, trust, compliance, and protection measures.",
        ),
        section(
            "Benefits",
            purpose="Present the key benefits and outcomes for customers.",
        ),
        section(
            "Trust",
            required=False,
            purpose="Provide evidence of reliability through customers, metrics, or credentials.",
        ),
        section(
            "CTA",
            purpose="Guide visitors toward signup, consultation, or another conversion action.",
        ),
    ),
    multi_page=(
        page(
            "Home",
            purpose="Introduce the fintech offering and establish its core value proposition.",
        ),
        page(
            "Solutions",
            purpose="Present the available financial solutions.",
            children=(
                collection(
                    "Solution",
                    purpose="Organize individual financial solutions.",
                    item_template="Solution",
                ),
            ),
        ),
        entry_point(
            "Solution",
            purpose="Provide direct access to individual financial solution pages.",
            target_template="Solution",
        ),
        page(
            "Security",
            purpose="Explain security, compliance, privacy, and trust measures.",
        ),
        page(
            "Company",
            required=False,
            purpose="Present the organization behind the financial product.",
        ),
        page(
            "Contact",
            required=False,
            purpose="Provide a way for customers or prospects to contact the organization.",
        ),
        page(
            "Login",
            required=False,
            purpose="Allow existing customers to access their financial account.",
        ),
        page(
            "Signup",
            required=False,
            purpose="Allow new customers to create an account.",
        ),
    ),
    single_page_links=(
        LinkRule("Hero", "Solutions", LinkType.NAVIGATION),
        LinkRule("Solutions", "How It Works", LinkType.NAVIGATION),
        LinkRule("How It Works", "Security", LinkType.NAVIGATION),
        LinkRule("Security", "Benefits", LinkType.NAVIGATION),
        LinkRule("Benefits", "Trust", LinkType.NAVIGATION),
        LinkRule("Trust", "CTA", LinkType.NAVIGATION),
        LinkRule("Hero", "CTA", LinkType.CTA),
    ),
    multi_page_links=(
        LinkRule("Home", "Solutions", LinkType.NAVIGATION),
        LinkRule("Home", "Security", LinkType.NAVIGATION),
        LinkRule("Home", "Company", LinkType.NAVIGATION),
        LinkRule("Home", "Contact", LinkType.NAVIGATION),
        LinkRule("Home", "Login", LinkType.NAVIGATION),
        LinkRule("Solutions", "Solution", LinkType.NAVIGATION),
        LinkRule("Solution", "Signup", LinkType.CTA),
        LinkRule("Security", "Signup", LinkType.CTA),
    ),
    templates=FINTECH_TEMPLATES,
)


# ---------------------------------------------------------------------------
# Technology
# ---------------------------------------------------------------------------


TECHNOLOGY_TEMPLATES = (
    template(
        "Product",
        purpose="Present an individual technology product, its capabilities, value, and use cases.",
    ),
    template(
        "Use Case",
        purpose="Present an individual problem or scenario and explain how the technology addresses it.",
    ),
)


TECHNOLOGY = profile(
    site_type=SiteType.TECHNOLOGY,
    default_topology=Topology.HIERARCHICAL,
    single_page=(
        section(
            "Hero",
            purpose="Introduce the technology offering and communicate its core value.",
        ),
        section(
            "Products",
            purpose="Present the main technology products or capabilities.",
        ),
        section(
            "Use Cases",
            purpose="Show how the technology can be applied to specific scenarios.",
        ),
        section(
            "Technology",
            purpose="Explain the underlying technology, architecture, or technical advantages.",
        ),
        section(
            "Security",
            required=False,
            purpose="Explain security, reliability, privacy, and technical safeguards.",
        ),
        section(
            "Resources",
            required=False,
            purpose="Provide technical and educational resources.",
        ),
        section(
            "CTA",
            purpose="Guide visitors toward trying, purchasing, contacting, or learning more.",
        ),
    ),
    multi_page=(
        page(
            "Home",
            purpose="Introduce the technology company and its primary offering.",
        ),
        page(
            "Products",
            purpose="Present the technology products.",
            children=(
                collection(
                    "Product",
                    purpose="Organize individual technology products.",
                    item_template="Product",
                ),
            ),
        ),
        entry_point(
            "Product",
            purpose="Provide direct access to individual technology product pages.",
            target_template="Product",
        ),
        page(
            "Use Cases",
            purpose="Present technology applications and use cases.",
            children=(
                collection(
                    "Use Case",
                    purpose="Organize individual technology use cases.",
                    item_template="Use Case",
                ),
            ),
        ),
        entry_point(
            "Use Case",
            purpose="Provide direct access to individual technology use case pages.",
            target_template="Use Case",
        ),
        page(
            "Technology",
            purpose="Explain the underlying technology and technical capabilities.",
        ),
        page(
            "Resources",
            required=False,
            purpose="Provide documentation, articles, guides, and technical resources.",
        ),
        page(
            "Company",
            required=False,
            purpose="Present the organization behind the technology.",
        ),
        page(
            "Contact",
            required=False,
            purpose="Provide a way to contact the technology company.",
        ),
    ),
    single_page_links=(
        LinkRule("Hero", "Products", LinkType.NAVIGATION),
        LinkRule("Products", "Use Cases", LinkType.NAVIGATION),
        LinkRule("Use Cases", "Technology", LinkType.NAVIGATION),
        LinkRule("Technology", "Security", LinkType.NAVIGATION),
        LinkRule("Security", "Resources", LinkType.NAVIGATION),
        LinkRule("Resources", "CTA", LinkType.NAVIGATION),
        LinkRule("Hero", "CTA", LinkType.CTA),
    ),
    multi_page_links=(
        LinkRule("Home", "Products", LinkType.NAVIGATION),
        LinkRule("Home", "Use Cases", LinkType.NAVIGATION),
        LinkRule("Home", "Technology", LinkType.NAVIGATION),
        LinkRule("Home", "Resources", LinkType.NAVIGATION),
        LinkRule("Home", "Company", LinkType.NAVIGATION),
        LinkRule("Home", "Contact", LinkType.NAVIGATION),
        LinkRule("Products", "Product", LinkType.NAVIGATION),
        LinkRule("Use Cases", "Use Case", LinkType.NAVIGATION),
        LinkRule("Product", "Contact", LinkType.CTA),
        LinkRule("Use Case", "Product", LinkType.CTA),
    ),
    templates=TECHNOLOGY_TEMPLATES,
)


# ---------------------------------------------------------------------------
# Fashion
# ---------------------------------------------------------------------------


FASHION_TEMPLATES = (
    template(
        "Collection",
        purpose="Present an individual fashion collection, its concept, products, and visual identity.",
    ),
    template(
        "Product",
        purpose="Present an individual fashion product, its details, variants, and purchasing actions.",
    ),
)


FASHION = profile(
    site_type=SiteType.FASHION,
    default_topology=Topology.MATRIX,
    single_page=(
        section(
            "Hero",
            purpose="Establish the fashion brand identity and introduce the current offering.",
        ),
        section(
            "Collections",
            purpose="Present the brand's collections and visual direction.",
        ),
        section(
            "Featured Products",
            purpose="Highlight selected products and encourage product discovery.",
        ),
        section(
            "Story",
            required=False,
            purpose="Communicate the brand story, philosophy, and creative identity.",
        ),
        section(
            "Journal",
            required=False,
            purpose="Present editorial stories, campaigns, inspiration, and brand content.",
        ),
        section(
            "Stores",
            required=False,
            purpose="Provide information about physical stores or retail locations.",
        ),
        section(
            "CTA",
            purpose="Guide visitors toward shopping, collection discovery, or another primary action.",
        ),
    ),
    multi_page=(
        page(
            "Home",
            purpose="Introduce the fashion brand and current offering.",
        ),
        page(
            "Collections",
            purpose="Present the brand's fashion collections.",
            children=(
                collection(
                    "Collection",
                    purpose="Organize individual fashion collections.",
                    item_template="Collection",
                ),
            ),
        ),
        entry_point(
            "Collection",
            purpose="Provide direct access to individual fashion collection pages.",
            target_template="Collection",
        ),
        page(
            "Shop",
            purpose="Provide access to the product catalog.",
            children=(
                collection(
                    "Category",
                    purpose="Organize fashion products into meaningful shopping categories.",
                    item_template="Product",
                ),
            ),
        ),
        entry_point(
            "Product",
            purpose="Provide direct access to individual fashion product pages.",
            target_template="Product",
        ),
        page(
            "Journal",
            required=False,
            purpose="Publish fashion stories, campaigns, inspiration, and editorial content.",
        ),
        page(
            "Stores",
            required=False,
            purpose="Present physical stores and retail locations.",
        ),
        page(
            "About",
            required=False,
            purpose="Present the fashion brand, its story, values, and identity.",
        ),
        page(
            "Contact",
            required=False,
            purpose="Provide a way to contact the fashion brand.",
        ),
    ),
    single_page_links=(
        LinkRule("Hero", "Collections", LinkType.NAVIGATION),
        LinkRule("Collections", "Featured Products", LinkType.NAVIGATION),
        LinkRule("Featured Products", "Story", LinkType.NAVIGATION),
        LinkRule("Story", "Journal", LinkType.NAVIGATION),
        LinkRule("Journal", "Stores", LinkType.NAVIGATION),
        LinkRule("Stores", "CTA", LinkType.NAVIGATION),
        LinkRule("Hero", "CTA", LinkType.CTA),
    ),
    multi_page_links=(
        LinkRule("Home", "Collections", LinkType.NAVIGATION),
        LinkRule("Home", "Shop", LinkType.NAVIGATION),
        LinkRule("Home", "Journal", LinkType.NAVIGATION),
        LinkRule("Home", "Stores", LinkType.NAVIGATION),
        LinkRule("Home", "About", LinkType.NAVIGATION),
        LinkRule("Home", "Contact", LinkType.NAVIGATION),
        LinkRule("Collections", "Collection", LinkType.NAVIGATION),
        LinkRule("Shop", "Product", LinkType.NAVIGATION),
        LinkRule("Collection", "Product", LinkType.CTA),
        LinkRule("Product", "Shop", LinkType.CTA),
    ),
    templates=FASHION_TEMPLATES,
)


# ---------------------------------------------------------------------------
# Profile registry
# ---------------------------------------------------------------------------


PROFILES: dict[SiteType, SiteProfile] = {
    SiteType.LANDING_PAGE: LANDING_PAGE,
    SiteType.SAAS: SAAS,
    SiteType.AGENCY: AGENCY,
    SiteType.PORTFOLIO: PORTFOLIO,
    SiteType.ECOMMERCE: ECOMMERCE,
    SiteType.TRAVEL: TRAVEL,
    SiteType.WELLNESS: WELLNESS,
    SiteType.FINTECH: FINTECH,
    SiteType.TECHNOLOGY: TECHNOLOGY,
    SiteType.FASHION: FASHION,
}