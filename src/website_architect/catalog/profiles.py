from website_architect.domain.enums import LinkType, NodeType, SiteType, Topology
from website_architect.domain.nodes import PageDefinition

from .definitions import LinkRule, SiteProfile, profile


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
    repeatable: bool = False,
    children: tuple[PageDefinition, ...] = (),
) -> PageDefinition:
    return PageDefinition(
        name=name,
        node_type=NodeType.PAGE,
        required=required,
        repeatable=repeatable,
        purpose=purpose,
        children=children,
    )


def template(
    name: str,
    *,
    purpose: str,
    required: bool = True,
    children: tuple[PageDefinition, ...] = (),
) -> PageDefinition:
    return PageDefinition(
        name=name,
        node_type=NodeType.TEMPLATE,
        required=required,
        repeatable=True,
        purpose=purpose,
        children=children,
    )


def collection(
    name: str,
    *,
    purpose: str,
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
    )


# ---------------------------------------------------------------------------
# Landing Page
# ---------------------------------------------------------------------------


LANDING_PAGE = profile(
    site_type=SiteType.LANDING_PAGE,
    topology=Topology.SEQUENTIAL,
    single_page=(
        section(
            "Hero",
            purpose="Introduce the offering, communicate its primary value proposition, and drive the user's initial action.",
        ),
        section(
            "Value Proposition",
            purpose="Explain the primary value the offering provides and why it is relevant to the target audience.",
        ),
        section(
            "Problem",
            required=False,
            purpose="Describe the problem, need, or pain point that the offering addresses.",
        ),
        section(
            "Solution",
            purpose="Explain how the offering solves the problem and delivers the promised value.",
        ),
        section(
            "Features",
            required=False,
            purpose="Present the key capabilities and characteristics of the offering.",
        ),
        section(
            "Benefits",
            required=False,
            purpose="Translate the offering's capabilities into concrete benefits for the user.",
        ),
        section(
            "Social Proof",
            required=False,
            purpose="Build credibility by presenting evidence that other people or organizations trust the offering.",
        ),
        section(
            "Testimonials",
            required=False,
            purpose="Provide direct customer feedback that reinforces trust and validates the offering.",
        ),
        section(
            "Pricing",
            required=False,
            purpose="Communicate the cost and available purchasing or subscription options.",
        ),
        section(
            "FAQ",
            required=False,
            purpose="Address common questions and remove uncertainty before the user's decision.",
        ),
        section(
            "CTA",
            purpose="Provide a clear final action that moves the user toward conversion.",
        ),
    ),
    multi_page=(
        page(
            "Product",
            required=False,
            purpose="Present the offering in greater detail and explain its capabilities and value.",
        ),
        page(
            "Features",
            required=False,
            purpose="Provide a dedicated overview of the offering's key features and capabilities.",
        ),
        page(
            "Pricing",
            required=False,
            purpose="Present pricing options and help users understand the commercial model.",
        ),
        page(
            "About",
            required=False,
            purpose="Explain who is behind the offering and establish organizational credibility.",
        ),
        page(
            "FAQ",
            required=False,
            purpose="Answer common questions and address objections or uncertainty.",
        ),
        page(
            "Contact",
            required=False,
            purpose="Provide a way for users to initiate direct communication with the organization.",
        ),
    ),
    single_page_links=(
        LinkRule("Hero", "Value Proposition", LinkType.NAVIGATION),
        LinkRule("Value Proposition", "Solution", LinkType.NAVIGATION),
        LinkRule("Solution", "Features", LinkType.NAVIGATION),
        LinkRule("Features", "Social Proof", LinkType.NAVIGATION),
        LinkRule("Social Proof", "Pricing", LinkType.NAVIGATION),
        LinkRule("Pricing", "FAQ", LinkType.NAVIGATION),
        LinkRule("FAQ", "CTA", LinkType.NAVIGATION),
        LinkRule("Hero", "CTA", LinkType.CTA),
        LinkRule("Pricing", "CTA", LinkType.CTA),
    ),
    multi_page_links=(
        LinkRule("Home", "Product", LinkType.NAVIGATION),
        LinkRule("Home", "Features", LinkType.NAVIGATION),
        LinkRule("Home", "Pricing", LinkType.NAVIGATION),
        LinkRule("Home", "About", LinkType.NAVIGATION),
        LinkRule("Home", "Contact", LinkType.NAVIGATION),
        LinkRule("Product", "Contact", LinkType.CTA),
        LinkRule("Pricing", "Contact", LinkType.CTA),
    ),
)


# ---------------------------------------------------------------------------
# SaaS
# ---------------------------------------------------------------------------


SAAS = profile(
    site_type=SiteType.SAAS,
    topology=Topology.HIERARCHICAL,
    single_page=(
        section(
            "Hero",
            purpose="Introduce the SaaS product, communicate its core value, and drive users toward adoption.",
        ),
        section(
            "Product Overview",
            purpose="Explain what the product does, who it serves, and the primary value it provides.",
        ),
        section(
            "Features",
            purpose="Present the product's main capabilities and explain how they support user needs.",
        ),
        section(
            "Integrations",
            required=False,
            purpose="Show how the product connects with external tools, platforms, or services.",
        ),
        section(
            "Security",
            required=False,
            purpose="Explain how the product protects user data, systems, and business information.",
        ),
        section(
            "Use Cases",
            required=False,
            purpose="Demonstrate how different users, teams, or organizations can apply the product.",
        ),
        section(
            "Testimonials",
            required=False,
            purpose="Provide customer evidence that validates the product's value and reliability.",
        ),
        section(
            "Pricing",
            purpose="Present subscription or commercial plans and help users evaluate the available options.",
        ),
        section(
            "FAQ",
            required=False,
            purpose="Answer common product, pricing, implementation, and purchasing questions.",
        ),
        section(
            "CTA",
            purpose="Drive users toward starting a trial, creating an account, booking a demo, or taking another conversion action.",
        ),
    ),
    multi_page=(
        page(
            "Product",
            purpose="Provide a dedicated area describing the SaaS product and its capabilities.",
            children=(
                page(
                    "Overview",
                    purpose="Explain the product's core value, functionality, and positioning.",
                ),
                page(
                    "Features",
                    purpose="Provide detailed information about the product's capabilities.",
                ),
                page(
                    "Integrations",
                    required=False,
                    purpose="Document supported integrations and explain how the product connects with external systems.",
                ),
                page(
                    "Security",
                    required=False,
                    purpose="Explain the product's security architecture, practices, and protections.",
                ),
            ),
        ),
        page(
            "Solutions",
            required=False,
            purpose="Organize product applications around the needs of different customer segments.",
            children=(
                page(
                    "Startups",
                    purpose="Explain how the product addresses the needs and constraints of startups.",
                ),
                page(
                    "Teams",
                    purpose="Explain how the product supports collaborative teams and their workflows.",
                ),
                page(
                    "Enterprise",
                    purpose="Explain how the product addresses enterprise-scale requirements and organizational complexity.",
                ),
            ),
        ),
        page(
            "Pricing",
            purpose="Present subscription plans, pricing options, and commercial differences between tiers.",
        ),
        page(
            "Resources",
            required=False,
            purpose="Provide educational, informational, and product-supporting resources.",
            children=(
                page(
                    "Blog",
                    purpose="Publish ongoing articles, insights, announcements, and educational content.",
                ),
                page(
                    "Documentation",
                    purpose="Provide detailed technical and product documentation for users and developers.",
                ),
                page(
                    "Guides",
                    purpose="Provide practical guidance for using the product or solving specific problems.",
                ),
                page(
                    "Changelog",
                    purpose="Communicate product updates, releases, improvements, and changes.",
                ),
            ),
        ),
        page(
            "Company",
            required=False,
            purpose="Provide information about the organization behind the product.",
            children=(
                page(
                    "About",
                    purpose="Explain the organization's identity, mission, and background.",
                ),
                page(
                    "Careers",
                    purpose="Present employment opportunities and information for potential candidates.",
                ),
                page(
                    "Contact",
                    purpose="Provide a way for users and prospects to communicate directly with the organization.",
                ),
            ),
        ),
        page(
            "Login",
            purpose="Allow existing users to access their product account.",
        ),
        page(
            "Signup",
            purpose="Allow new users to create an account and begin using the product.",
        ),
    ),
    single_page_links=(
        LinkRule("Hero", "Product Overview", LinkType.NAVIGATION),
        LinkRule("Product Overview", "Features", LinkType.NAVIGATION),
        LinkRule("Features", "Integrations", LinkType.NAVIGATION),
        LinkRule("Features", "Security", LinkType.NAVIGATION),
        LinkRule("Security", "Pricing", LinkType.NAVIGATION),
        LinkRule("Pricing", "FAQ", LinkType.NAVIGATION),
        LinkRule("FAQ", "CTA", LinkType.NAVIGATION),
        LinkRule("Hero", "CTA", LinkType.CTA),
        LinkRule("Pricing", "CTA", LinkType.CTA),
    ),
    multi_page_links=(
        LinkRule("Home", "Product", LinkType.NAVIGATION),
        LinkRule("Home", "Solutions", LinkType.NAVIGATION),
        LinkRule("Home", "Pricing", LinkType.NAVIGATION),
        LinkRule("Home", "Resources", LinkType.NAVIGATION),
        LinkRule("Home", "Company", LinkType.NAVIGATION),
        LinkRule("Home", "Login", LinkType.NAVIGATION),
        LinkRule("Product", "Signup", LinkType.CTA),
        LinkRule("Pricing", "Signup", LinkType.CTA),
        LinkRule("Solutions", "Signup", LinkType.CTA),
        LinkRule("Company", "Company.Contact", LinkType.NAVIGATION),
    ),
)


# ---------------------------------------------------------------------------
# Agency
# ---------------------------------------------------------------------------


AGENCY = profile(
    site_type=SiteType.AGENCY,
    topology=Topology.HIERARCHICAL,
    single_page=(
        section(
            "Hero",
            purpose="Introduce the agency, communicate its positioning, and drive visitors toward engagement.",
        ),
        section(
            "Services",
            purpose="Present the agency's capabilities and the services it provides to clients.",
        ),
        section(
            "Work",
            purpose="Showcase selected client work and demonstrate the agency's capabilities through outcomes.",
        ),
        section(
            "About",
            purpose="Explain the agency's identity, expertise, background, and approach.",
        ),
        section(
            "Process",
            required=False,
            purpose="Explain how the agency works with clients from initial engagement through delivery.",
        ),
        section(
            "Clients",
            required=False,
            purpose="Demonstrate the organizations and brands that have worked with the agency.",
        ),
        section(
            "Testimonials",
            required=False,
            purpose="Provide client feedback that reinforces trust and demonstrates the quality of the agency's work.",
        ),
        section(
            "Team",
            required=False,
            purpose="Introduce the people responsible for delivering the agency's expertise and services.",
        ),
        section(
            "FAQ",
            required=False,
            purpose="Address common questions about services, process, pricing, and collaboration.",
        ),
        section(
            "Contact",
            purpose="Provide a direct path for prospective clients to initiate a conversation with the agency.",
        ),
    ),
    multi_page=(
        page(
            "Services",
            purpose="Present the agency's service offering and areas of expertise.",
            children=(
                template(
                    "Service",
                    purpose="Provide a reusable structure for presenting an individual agency service.",
                ),
            ),
        ),
        page(
            "Work",
            purpose="Organize and showcase the agency's portfolio of client work.",
            children=(
                template(
                    "Case Study",
                    purpose="Present an individual project, its context, approach, and results.",
                ),
            ),
        ),
        page(
            "About",
            purpose="Explain the agency's identity, values, expertise, and operating approach.",
            children=(
                page(
                    "Team",
                    required=False,
                    purpose="Introduce the agency's team and individual areas of expertise.",
                ),
                page(
                    "Process",
                    required=False,
                    purpose="Explain the agency's methodology and collaboration process.",
                ),
                page(
                    "Values",
                    required=False,
                    purpose="Communicate the principles and values that guide the agency's work.",
                ),
            ),
        ),
        page(
            "Insights",
            required=False,
            purpose="Publish knowledge, perspectives, and educational content that demonstrates the agency's expertise.",
            children=(
                page(
                    "Blog",
                    required=False,
                    purpose="Publish ongoing agency perspectives, articles, and insights.",
                ),
                page(
                    "Articles",
                    required=False,
                    purpose="Provide deeper editorial content focused on relevant topics and expertise.",
                ),
            ),
        ),
        page(
            "Contact",
            purpose="Provide a direct communication channel for prospective and existing clients.",
        ),
    ),
    single_page_links=(
        LinkRule("Hero", "Services", LinkType.NAVIGATION),
        LinkRule("Services", "Work", LinkType.NAVIGATION),
        LinkRule("Work", "About", LinkType.NAVIGATION),
        LinkRule("About", "Testimonials", LinkType.NAVIGATION),
        LinkRule("Testimonials", "Contact", LinkType.NAVIGATION),
        LinkRule("Hero", "Contact", LinkType.CTA),
        LinkRule("Work", "Contact", LinkType.CTA),
    ),
    multi_page_links=(
        LinkRule("Home", "Services", LinkType.NAVIGATION),
        LinkRule("Home", "Work", LinkType.NAVIGATION),
        LinkRule("Home", "About", LinkType.NAVIGATION),
        LinkRule("Home", "Insights", LinkType.NAVIGATION),
        LinkRule("Home", "Contact", LinkType.NAVIGATION),
        LinkRule("Services", "Contact", LinkType.CTA),
        LinkRule("Work", "Contact", LinkType.CTA),
    ),
)


# ---------------------------------------------------------------------------
# Portfolio
# ---------------------------------------------------------------------------


PORTFOLIO = profile(
    site_type=SiteType.PORTFOLIO,
    topology=Topology.SEQUENTIAL,
    single_page=(
        section(
            "Hero",
            purpose="Introduce the creator or professional and communicate their primary positioning and expertise.",
        ),
        section(
            "About",
            purpose="Provide background information about the creator, professional, or studio.",
        ),
        section(
            "Selected Work",
            purpose="Showcase the most relevant projects and demonstrate the creator's capabilities.",
        ),
        section(
            "Skills",
            required=False,
            purpose="Present the creator's core skills, capabilities, and areas of expertise.",
        ),
        section(
            "Experience",
            required=False,
            purpose="Summarize relevant professional experience, roles, and career background.",
        ),
        section(
            "Testimonials",
            required=False,
            purpose="Provide feedback from clients, collaborators, or employers to reinforce credibility.",
        ),
        section(
            "Contact",
            purpose="Provide a direct way for visitors to initiate professional communication.",
        ),
    ),
    multi_page=(
        page(
            "Work",
            purpose="Provide a dedicated portfolio of projects and professional work.",
            children=(
                template(
                    "Project",
                    purpose="Present an individual project, its context, contribution, process, and outcome.",
                ),
            ),
        ),
        page(
            "About",
            purpose="Explain the creator's identity, background, positioning, and professional profile.",
        ),
        page(
            "Experience",
            required=False,
            purpose="Present the creator's professional history, roles, and relevant experience.",
        ),
        page(
            "Skills",
            required=False,
            purpose="Present the creator's professional skills and areas of expertise.",
        ),
        page(
            "Journal",
            required=False,
            purpose="Publish personal insights, writing, experiments, or professional reflections.",
        ),
        page(
            "Contact",
            purpose="Provide a direct channel for professional inquiries and collaboration.",
        ),
    ),
    single_page_links=(
        LinkRule("Hero", "About", LinkType.NAVIGATION),
        LinkRule("About", "Selected Work", LinkType.NAVIGATION),
        LinkRule("Selected Work", "Skills", LinkType.NAVIGATION),
        LinkRule("Skills", "Experience", LinkType.NAVIGATION),
        LinkRule("Experience", "Testimonials", LinkType.NAVIGATION),
        LinkRule("Testimonials", "Contact", LinkType.NAVIGATION),
        LinkRule("Hero", "Selected Work", LinkType.CTA),
        LinkRule("Selected Work", "Contact", LinkType.CTA),
    ),
    multi_page_links=(
        LinkRule("Home", "Work", LinkType.NAVIGATION),
        LinkRule("Home", "About", LinkType.NAVIGATION),
        LinkRule("Home", "Experience", LinkType.NAVIGATION),
        LinkRule("Home", "Skills", LinkType.NAVIGATION),
        LinkRule("Home", "Journal", LinkType.NAVIGATION),
        LinkRule("Home", "Contact", LinkType.NAVIGATION),
        LinkRule("Work", "Contact", LinkType.CTA),
    ),
)


# ---------------------------------------------------------------------------
# Ecommerce
# ---------------------------------------------------------------------------


ECOMMERCE = profile(
    site_type=SiteType.ECOMMERCE,
    topology=Topology.MATRIX,
    single_page=(
        section(
            "Hero",
            purpose="Introduce the store, establish the brand proposition, and direct users toward product discovery.",
        ),
        section(
            "Featured Products",
            purpose="Highlight selected products that the store wants users to discover or consider.",
        ),
        section(
            "Categories",
            purpose="Help users discover products through the store's main product categories.",
        ),
        section(
            "Collections",
            required=False,
            purpose="Present curated groups of products organized around themes, campaigns, or merchandising concepts.",
        ),
        section(
            "Best Sellers",
            required=False,
            purpose="Highlight products with strong demand or popularity to guide product discovery.",
        ),
        section(
            "New Arrivals",
            required=False,
            purpose="Showcase recently introduced products and encourage users to explore new inventory.",
        ),
        section(
            "Offers",
            required=False,
            purpose="Communicate promotions, discounts, or commercial opportunities available to shoppers.",
        ),
        section(
            "Reviews",
            required=False,
            purpose="Provide customer feedback and social proof to support product evaluation and purchasing decisions.",
        ),
        section(
            "CTA",
            purpose="Direct users toward shopping, product discovery, or another primary commercial action.",
        ),
    ),
    multi_page=(
        page(
            "Shop",
            purpose="Provide the main product discovery and browsing experience for the store.",
            children=(
                collection(
                    "Category",
                    purpose="Organize products into meaningful categories to support browsing and discovery.",
                    children=(
                        template(
                            "Product",
                            purpose="Present an individual product, its information, options, and purchasing actions.",
                        ),
                    ),
                ),
                collection(
                    "Collections",
                    required=False,
                    purpose="Organize curated groups of products around themes, campaigns, or merchandising strategies.",
                    children=(
                        template(
                            "Collection",
                            purpose="Present a curated group of products around a common theme or merchandising concept.",
                        ),
                    ),
                ),
                page(
                    "Search",
                    required=False,
                    purpose="Allow users to search, filter, and discover products across the catalog.",
                ),
            ),
        ),
        template(
            "Product",
            purpose="Present an individual product and support product evaluation and purchase.",
        ),
        page(
            "Wishlist",
            required=False,
            purpose="Allow users to save and revisit products they are interested in purchasing.",
        ),
        page(
            "Cart",
            purpose="Review selected products, quantities, prices, and prepare the order for checkout.",
        ),
        page(
            "Checkout",
            purpose="Complete the purchase by collecting order, shipping, billing, and payment information.",
        ),
        page(
            "Account",
            required=False,
            purpose="Provide authenticated users with access to their profile, orders, addresses, and account settings.",
            children=(
                page(
                    "Profile",
                    purpose="Allow users to view and manage their personal account information.",
                ),
                page(
                    "Orders",
                    purpose="Allow users to review their current and previous orders.",
                ),
                page(
                    "Addresses",
                    purpose="Allow users to manage their saved shipping and billing addresses.",
                ),
            ),
        ),
        page(
            "Journal",
            required=False,
            purpose="Publish editorial content, brand stories, product inspiration, or other content supporting the shopping experience.",
        ),
        page(
            "Support",
            required=False,
            purpose="Provide assistance and information for customers before, during, or after a purchase.",
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
        LinkRule("Home", "Wishlist", LinkType.NAVIGATION),
        LinkRule("Home", "Cart", LinkType.NAVIGATION),
        LinkRule("Home", "Account", LinkType.NAVIGATION),
        LinkRule("Home", "Journal", LinkType.NAVIGATION),
        LinkRule("Shop", "Shop.Category.Product", LinkType.NAVIGATION),
        LinkRule("Shop.Category.Product", "Wishlist", LinkType.CTA),
        LinkRule("Shop.Category.Product", "Cart", LinkType.CTA),
        LinkRule("Cart", "Checkout", LinkType.NAVIGATION),
        LinkRule("Checkout", "Account", LinkType.NAVIGATION),
        LinkRule("Journal", "Shop", LinkType.CTA),
    ),
)


# ---------------------------------------------------------------------------
# Travel
# ---------------------------------------------------------------------------


TRAVEL = profile(
    site_type=SiteType.TRAVEL,
    topology=Topology.MATRIX,
    single_page=(
        section(
            "Hero",
            purpose="Introduce the travel offering and inspire users to explore destinations and experiences.",
        ),
        section(
            "Destination",
            purpose="Present a featured destination and communicate its primary attractions and value.",
        ),
        section(
            "Experiences",
            purpose="Showcase activities, experiences, and things users can do within the destination.",
        ),
        section(
            "Highlights",
            purpose="Surface the most important or memorable aspects of the destination or travel offering.",
        ),
        section(
            "Itinerary",
            required=False,
            purpose="Present a suggested sequence of activities, destinations, or travel experiences.",
        ),
        section(
            "Accommodation",
            required=False,
            purpose="Present available places to stay and relevant accommodation information.",
        ),
        section(
            "Gallery",
            required=False,
            purpose="Provide visual inspiration and contextual imagery for destinations and experiences.",
        ),
        section(
            "Reviews",
            required=False,
            purpose="Provide traveler feedback and social proof to build confidence in the travel offering.",
        ),
        section(
            "FAQ",
            required=False,
            purpose="Address common questions about destinations, experiences, logistics, and booking.",
        ),
        section(
            "Booking CTA",
            purpose="Drive users toward booking, inquiry, or another travel conversion action.",
        ),
    ),
    multi_page=(
        page(
            "Destinations",
            purpose="Provide the main discovery experience for exploring available travel destinations.",
            children=(
                collection(
                    "Destination",
                    purpose="Organize and present individual destinations available to travelers.",
                    children=(
                        page(
                            "Overview",
                            purpose="Present the destination's essential information, highlights, and positioning.",
                        ),
                        collection(
                            "Places",
                            required=False,
                            purpose="Organize notable places, attractions, and points of interest within a destination.",
                        ),
                        collection(
                            "Experiences",
                            required=False,
                            purpose="Organize activities and experiences available within a destination.",
                        ),
                        collection(
                            "Accommodation",
                            required=False,
                            purpose="Organize accommodation options available within a destination.",
                        ),
                        collection(
                            "Itineraries",
                            required=False,
                            purpose="Organize suggested travel itineraries associated with a destination.",
                        ),
                    ),
                ),
            ),
        ),
        page(
            "Experiences",
            purpose="Provide a dedicated discovery area for travel experiences and activities.",
            children=(
                template(
                    "Experience",
                    purpose="Present an individual travel experience, its details, value, and booking information.",
                ),
                collection(
                    "Categories",
                    required=False,
                    purpose="Organize travel experiences into meaningful categories for discovery.",
                ),
            ),
        ),
        page(
            "Itineraries",
            required=False,
            purpose="Provide structured travel plans that combine destinations, activities, and timing.",
            children=(
                template(
                    "Itinerary",
                    purpose="Present an individual travel itinerary with its sequence of destinations and activities.",
                ),
            ),
        ),
        page(
            "Journal",
            required=False,
            purpose="Publish travel stories, inspiration, guides, and editorial content.",
        ),
        page(
            "About",
            required=False,
            purpose="Explain the organization, brand, or people behind the travel offering.",
        ),
        page(
            "Contact",
            required=False,
            purpose="Provide a direct channel for travel inquiries, assistance, and communication.",
        ),
        page(
            "Booking",
            purpose="Allow users to initiate or complete a booking for a travel offering.",
        ),
    ),
    single_page_links=(
        LinkRule("Hero", "Destination", LinkType.NAVIGATION),
        LinkRule("Destination", "Experiences", LinkType.NAVIGATION),
        LinkRule("Experiences", "Highlights", LinkType.NAVIGATION),
        LinkRule("Highlights", "Itinerary", LinkType.NAVIGATION),
        LinkRule("Itinerary", "Accommodation", LinkType.NAVIGATION),
        LinkRule("Accommodation", "Reviews", LinkType.NAVIGATION),
        LinkRule("Reviews", "Booking CTA", LinkType.NAVIGATION),
        LinkRule("Hero", "Booking CTA", LinkType.CTA),
        LinkRule("Experiences", "Booking CTA", LinkType.CTA),
    ),
    multi_page_links=(
        LinkRule("Home", "Destinations", LinkType.NAVIGATION),
        LinkRule("Home", "Experiences", LinkType.NAVIGATION),
        LinkRule("Home", "Itineraries", LinkType.NAVIGATION),
        LinkRule("Home", "Journal", LinkType.NAVIGATION),
        LinkRule("Home", "About", LinkType.NAVIGATION),
        LinkRule("Home", "Booking", LinkType.NAVIGATION),
        LinkRule(
            "Destinations.Destination.Experiences",
            "Experiences.Experience",
            LinkType.NAVIGATION,
        ),
        LinkRule(
            "Destinations.Destination.Itineraries",
            "Itineraries.Itinerary",
            LinkType.NAVIGATION,
        ),
        LinkRule(
            "Experiences.Experience",
            "Destinations.Destination",
            LinkType.NAVIGATION,
        ),
        LinkRule(
            "Experiences.Experience",
            "Booking",
            LinkType.CTA,
        ),
        LinkRule(
            "Itineraries.Itinerary",
            "Booking",
            LinkType.CTA,
        ),
        LinkRule("Journal", "Destinations", LinkType.NAVIGATION),
    ),
)


# ---------------------------------------------------------------------------
# Wellness
# ---------------------------------------------------------------------------


WELLNESS = profile(
    site_type=SiteType.WELLNESS,
    topology=Topology.HIERARCHICAL,
    single_page=(
        section(
            "Hero",
            purpose="Introduce the wellness offering, communicate its philosophy, and guide users toward engagement.",
        ),
        section(
            "Philosophy",
            purpose="Explain the principles, beliefs, and approach that define the wellness offering.",
        ),
        section(
            "Services",
            purpose="Present the wellness services available to users.",
        ),
        section(
            "Programs",
            required=False,
            purpose="Present structured wellness programs designed around specific goals or user needs.",
        ),
        section(
            "Benefits",
            required=False,
            purpose="Explain the outcomes and benefits users can expect from the services or programs.",
        ),
        section(
            "Team",
            required=False,
            purpose="Introduce the practitioners, specialists, or people delivering the wellness offering.",
        ),
        section(
            "Testimonials",
            required=False,
            purpose="Provide customer feedback that reinforces trust and demonstrates the value of the offering.",
        ),
        section(
            "Resources",
            required=False,
            purpose="Provide educational and informational content that supports users in their wellness journey.",
        ),
        section(
            "FAQ",
            required=False,
            purpose="Answer common questions about services, programs, process, and participation.",
        ),
        section(
            "Booking CTA",
            purpose="Drive users toward booking a service, consultation, program, or session.",
        ),
    ),
    multi_page=(
        page(
            "Services",
            purpose="Provide a dedicated overview of the wellness services available.",
            children=(
                template(
                    "Service",
                    purpose="Present an individual wellness service, its benefits, process, and participation information.",
                ),
            ),
        ),
        page(
            "Programs",
            required=False,
            purpose="Present structured wellness programs designed around specific goals or needs.",
            children=(
                template(
                    "Program",
                    purpose="Present an individual wellness program, its structure, goals, and participation details.",
                ),
            ),
        ),
        page(
            "About",
            purpose="Explain the organization's identity, philosophy, expertise, and approach to wellness.",
            children=(
                page(
                    "Philosophy",
                    required=False,
                    purpose="Explain the principles and beliefs that guide the organization's approach to wellness.",
                ),
                page(
                    "Team",
                    required=False,
                    purpose="Introduce the practitioners and specialists delivering the organization's services.",
                ),
                page(
                    "Approach",
                    required=False,
                    purpose="Explain the methodology and experience users can expect from the organization.",
                ),
            ),
        ),
        page(
            "Resources",
            required=False,
            purpose="Provide educational and informational content supporting users in their wellness journey.",
            children=(
                page(
                    "Blog",
                    required=False,
                    purpose="Publish ongoing wellness articles, insights, and educational content.",
                ),
                page(
                    "Guides",
                    required=False,
                    purpose="Provide practical guidance and educational resources around wellness topics.",
                ),
                page(
                    "Articles",
                    required=False,
                    purpose="Provide deeper editorial content about wellness topics and areas of expertise.",
                ),
            ),
        ),
        page(
            "Testimonials",
            required=False,
            purpose="Provide customer experiences and feedback that support trust and credibility.",
        ),
        page(
            "Contact",
            purpose="Provide a direct communication channel for questions, inquiries, and service-related contact.",
        ),
    ),
    single_page_links=(
        LinkRule("Hero", "Philosophy", LinkType.NAVIGATION),
        LinkRule("Philosophy", "Services", LinkType.NAVIGATION),
        LinkRule("Services", "Programs", LinkType.NAVIGATION),
        LinkRule("Programs", "Benefits", LinkType.NAVIGATION),
        LinkRule("Benefits", "Testimonials", LinkType.NAVIGATION),
        LinkRule("Testimonials", "FAQ", LinkType.NAVIGATION),
        LinkRule("FAQ", "Booking CTA", LinkType.NAVIGATION),
        LinkRule("Hero", "Booking CTA", LinkType.CTA),
        LinkRule("Services", "Booking CTA", LinkType.CTA),
    ),
    multi_page_links=(
        LinkRule("Home", "Services", LinkType.NAVIGATION),
        LinkRule("Home", "Programs", LinkType.NAVIGATION),
        LinkRule("Home", "About", LinkType.NAVIGATION),
        LinkRule("Home", "Resources", LinkType.NAVIGATION),
        LinkRule("Home", "Testimonials", LinkType.NAVIGATION),
        LinkRule("Home", "Contact", LinkType.NAVIGATION),
        LinkRule("Services", "Contact", LinkType.CTA),
        LinkRule("Programs", "Contact", LinkType.CTA),
        LinkRule("Resources", "Services", LinkType.CTA),
    ),
)


# ---------------------------------------------------------------------------
# Fintech
# ---------------------------------------------------------------------------


FINTECH = profile(
    site_type=SiteType.FINTECH,
    topology=Topology.HIERARCHICAL,
    single_page=(
        section(
            "Hero",
            purpose="Introduce the financial product, communicate its core value, and drive users toward adoption.",
        ),
        section(
            "Product",
            purpose="Explain the financial product, its purpose, and the value it provides to users.",
        ),
        section(
            "Features",
            purpose="Present the product's core financial capabilities and functionality.",
        ),
        section(
            "Security",
            purpose="Explain how financial data, transactions, and user accounts are protected.",
        ),
        section(
            "How It Works",
            purpose="Explain the main steps involved in using the financial product or service.",
        ),
        section(
            "Use Cases",
            required=False,
            purpose="Demonstrate how different user segments can apply the financial product.",
        ),
        section(
            "Integrations",
            required=False,
            purpose="Show how the financial product connects with external platforms, tools, or financial systems.",
        ),
        section(
            "Trust",
            purpose="Establish credibility through evidence, transparency, security information, or institutional trust signals.",
        ),
        section(
            "Pricing",
            required=False,
            purpose="Explain fees, pricing models, and commercial conditions associated with the financial product.",
        ),
        section(
            "FAQ",
            required=False,
            purpose="Address common questions about the financial product, security, pricing, and usage.",
        ),
        section(
            "CTA",
            purpose="Drive users toward account creation, product adoption, consultation, or another conversion action.",
        ),
    ),
    multi_page=(
        page(
            "Product",
            purpose="Provide a dedicated area explaining the financial product and its capabilities.",
            children=(
                page(
                    "Overview",
                    purpose="Explain the financial product's core value, purpose, and positioning.",
                ),
                page(
                    "Features",
                    purpose="Provide detailed information about the product's financial capabilities.",
                ),
                page(
                    "Security",
                    purpose="Explain security practices and protections for financial data and transactions.",
                ),
                page(
                    "Integrations",
                    required=False,
                    purpose="Explain how the product integrates with external financial or business systems.",
                ),
            ),
        ),
        page(
            "Solutions",
            required=False,
            purpose="Organize the financial offering around the needs of different customer segments.",
            children=(
                page(
                    "Individuals",
                    purpose="Explain how the financial product addresses individual customer needs.",
                ),
                page(
                    "Businesses",
                    purpose="Explain how the financial product addresses business and operational needs.",
                ),
                page(
                    "Enterprise",
                    purpose="Explain how the financial product addresses enterprise-scale financial requirements.",
                ),
            ),
        ),
        page(
            "Pricing",
            required=False,
            purpose="Present fees, pricing options, and commercial conditions for the financial product.",
        ),
        page(
            "Resources",
            required=False,
            purpose="Provide educational, informational, and product-supporting resources.",
            children=(
                page(
                    "Blog",
                    required=False,
                    purpose="Publish financial insights, product updates, and educational content.",
                ),
                page(
                    "Guides",
                    required=False,
                    purpose="Provide practical guidance for understanding or using the financial product.",
                ),
                page(
                    "Documentation",
                    required=False,
                    purpose="Provide detailed technical and product documentation for users and developers.",
                ),
            ),
        ),
        page(
            "Company",
            required=False,
            purpose="Provide information about the organization behind the financial product.",
            children=(
                page(
                    "About",
                    required=False,
                    purpose="Explain the organization's identity, mission, background, and credibility.",
                ),
                page(
                    "Careers",
                    required=False,
                    purpose="Present employment opportunities within the organization.",
                ),
                page(
                    "Contact",
                    purpose="Provide a direct channel for inquiries and communication with the organization.",
                ),
            ),
        ),
        page(
            "Security",
            purpose="Provide centralized information about security practices, protections, and trust.",
        ),
        page(
            "Login",
            purpose="Allow existing customers to securely access their financial account.",
        ),
        page(
            "Signup",
            purpose="Allow new customers to create an account and begin using the financial product.",
        ),
    ),
    single_page_links=(
        LinkRule("Hero", "Product", LinkType.NAVIGATION),
        LinkRule("Product", "Features", LinkType.NAVIGATION),
        LinkRule("Features", "Security", LinkType.NAVIGATION),
        LinkRule("Security", "How It Works", LinkType.NAVIGATION),
        LinkRule("How It Works", "Use Cases", LinkType.NAVIGATION),
        LinkRule("Use Cases", "Trust", LinkType.NAVIGATION),
        LinkRule("Trust", "Pricing", LinkType.NAVIGATION),
        LinkRule("Pricing", "FAQ", LinkType.NAVIGATION),
        LinkRule("FAQ", "CTA", LinkType.NAVIGATION),
        LinkRule("Hero", "CTA", LinkType.CTA),
        LinkRule("Pricing", "CTA", LinkType.CTA),
    ),
    multi_page_links=(
        LinkRule("Home", "Product", LinkType.NAVIGATION),
        LinkRule("Home", "Solutions", LinkType.NAVIGATION),
        LinkRule("Home", "Pricing", LinkType.NAVIGATION),
        LinkRule("Home", "Resources", LinkType.NAVIGATION),
        LinkRule("Home", "Company", LinkType.NAVIGATION),
        LinkRule("Home", "Security", LinkType.NAVIGATION),
        LinkRule("Home", "Login", LinkType.NAVIGATION),
        LinkRule("Product", "Product.Security", LinkType.NAVIGATION),
        LinkRule("Product", "Signup", LinkType.CTA),
        LinkRule("Pricing", "Signup", LinkType.CTA),
        LinkRule("Security", "Signup", LinkType.CTA),
    ),
)


# ---------------------------------------------------------------------------
# Technology
# ---------------------------------------------------------------------------


TECHNOLOGY = profile(
    site_type=SiteType.TECHNOLOGY,
    topology=Topology.HIERARCHICAL,
    single_page=(
        section(
            "Hero",
            purpose="Introduce the technology offering, communicate its core value, and direct users toward adoption or exploration.",
        ),
        section(
            "Technology",
            purpose="Explain the underlying technology, approach, or technical proposition behind the offering.",
        ),
        section(
            "Features",
            purpose="Present the primary capabilities and functionality of the technology product.",
        ),
        section(
            "Architecture",
            required=False,
            purpose="Explain the technical architecture and major components underlying the product.",
        ),
        section(
            "Use Cases",
            purpose="Demonstrate how the technology can be applied to practical problems or user needs.",
        ),
        section(
            "Integrations",
            required=False,
            purpose="Show how the technology connects with external tools, platforms, or systems.",
        ),
        section(
            "Performance",
            required=False,
            purpose="Communicate technical performance, scalability, reliability, or efficiency characteristics.",
        ),
        section(
            "Security",
            required=False,
            purpose="Explain how the technology protects systems, data, infrastructure, and users.",
        ),
        section(
            "Documentation",
            required=False,
            purpose="Provide technical information required to understand, integrate, configure, or use the technology.",
        ),
        section(
            "FAQ",
            required=False,
            purpose="Address common technical, product, implementation, and adoption questions.",
        ),
        section(
            "CTA",
            purpose="Drive users toward adoption, trial, documentation, contact, or another primary action.",
        ),
    ),
    multi_page=(
        page(
            "Technology",
            purpose="Provide detailed information about the technology and its technical foundation.",
            children=(
                page(
                    "Overview",
                    purpose="Explain the technology's purpose, value, and high-level capabilities.",
                ),
                page(
                    "Architecture",
                    required=False,
                    purpose="Document the technical architecture and structure of the technology.",
                ),
                page(
                    "Features",
                    purpose="Provide detailed information about the technology's capabilities.",
                ),
                page(
                    "Performance",
                    required=False,
                    purpose="Present technical performance, scalability, reliability, and efficiency information.",
                ),
            ),
        ),
        page(
            "Products",
            purpose="Organize the technology company's products and productized offerings.",
            children=(
                template(
                    "Product",
                    purpose="Present an individual technology product, its capabilities, value, and use cases.",
                ),
            ),
        ),
        page(
            "Solutions",
            required=False,
            purpose="Organize technology applications around specific business or technical problems.",
            children=(
                template(
                    "Use Case",
                    purpose="Present an individual problem or scenario and explain how the technology addresses it.",
                ),
            ),
        ),
        page(
            "Integrations",
            required=False,
            purpose="Present supported integrations and explain how the technology connects with external systems.",
        ),
        page(
            "Documentation",
            purpose="Provide detailed technical documentation for users, developers, and integrators.",
        ),
        page(
            "Resources",
            required=False,
            purpose="Provide educational and informational content supporting technology adoption.",
            children=(
                page(
                    "Blog",
                    required=False,
                    purpose="Publish technology insights, announcements, and educational articles.",
                ),
                page(
                    "Guides",
                    required=False,
                    purpose="Provide practical guidance for adopting, configuring, or using the technology.",
                ),
                page(
                    "Tutorials",
                    required=False,
                    purpose="Provide step-by-step educational material for learning and implementing the technology.",
                ),
            ),
        ),
        page(
            "Company",
            required=False,
            purpose="Provide information about the organization developing or providing the technology.",
            children=(
                page(
                    "About",
                    required=False,
                    purpose="Explain the organization's identity, mission, and background.",
                ),
                page(
                    "Careers",
                    required=False,
                    purpose="Present employment opportunities within the organization.",
                ),
                page(
                    "Contact",
                    required=False,
                    purpose="Provide a direct channel for technical, commercial, or organizational inquiries.",
                ),
            ),
        ),
        page(
            "Support",
            required=False,
            purpose="Provide assistance for users experiencing technical or product-related issues.",
        ),
    ),
    single_page_links=(
        LinkRule("Hero", "Technology", LinkType.NAVIGATION),
        LinkRule("Technology", "Features", LinkType.NAVIGATION),
        LinkRule("Features", "Architecture", LinkType.NAVIGATION),
        LinkRule("Architecture", "Use Cases", LinkType.NAVIGATION),
        LinkRule("Use Cases", "Integrations", LinkType.NAVIGATION),
        LinkRule("Integrations", "Performance", LinkType.NAVIGATION),
        LinkRule("Performance", "Security", LinkType.NAVIGATION),
        LinkRule("Security", "Documentation", LinkType.NAVIGATION),
        LinkRule("Documentation", "CTA", LinkType.NAVIGATION),
        LinkRule("Hero", "CTA", LinkType.CTA),
    ),
    multi_page_links=(
        LinkRule("Home", "Technology", LinkType.NAVIGATION),
        LinkRule("Home", "Products", LinkType.NAVIGATION),
        LinkRule("Home", "Solutions", LinkType.NAVIGATION),
        LinkRule("Home", "Integrations", LinkType.NAVIGATION),
        LinkRule("Home", "Documentation", LinkType.NAVIGATION),
        LinkRule("Home", "Resources", LinkType.NAVIGATION),
        LinkRule("Home", "Company", LinkType.NAVIGATION),
        LinkRule("Home", "Support", LinkType.NAVIGATION),
        LinkRule("Products", "Products.Product", LinkType.NAVIGATION),
        LinkRule("Products.Product", "Documentation", LinkType.CTA),
        LinkRule("Documentation", "Support", LinkType.CTA),
    ),
)


# ---------------------------------------------------------------------------
# Fashion
# ---------------------------------------------------------------------------


FASHION = profile(
    site_type=SiteType.FASHION,
    topology=Topology.MATRIX,
    single_page=(
        section(
            "Hero",
            purpose="Establish the fashion brand identity, communicate the collection proposition, and inspire exploration.",
        ),
        section(
            "Collection",
            purpose="Introduce the featured collection and communicate its visual and conceptual identity.",
        ),
        section(
            "Featured Products",
            purpose="Highlight selected products from the collection or current assortment.",
        ),
        section(
            "Editorial",
            required=False,
            purpose="Provide editorial storytelling that adds cultural, visual, or conceptual context to the brand.",
        ),
        section(
            "Story",
            required=False,
            purpose="Communicate the narrative, inspiration, or creative concept behind the brand or collection.",
        ),
        section(
            "Campaign",
            required=False,
            purpose="Present campaign content that communicates the seasonal or creative direction of the brand.",
        ),
        section(
            "Lookbook",
            required=False,
            purpose="Showcase curated looks and visual combinations that communicate the collection's styling.",
        ),
        section(
            "Stores",
            required=False,
            purpose="Help users discover physical retail locations and relevant store information.",
        ),
        section(
            "Newsletter",
            required=False,
            purpose="Provide a mechanism for users to subscribe to ongoing brand and collection communications.",
        ),
    ),
    multi_page=(
        page(
            "Collections",
            purpose="Provide access to the brand's collections and their visual and commercial stories.",
            children=(
                template(
                    "Collection",
                    purpose="Present an individual fashion collection, its concept, products, and visual identity.",
                ),
            ),
        ),
        page(
            "Shop",
            purpose="Provide the main product discovery and shopping experience.",
            children=(
                collection(
                    "Category",
                    purpose="Organize fashion products into meaningful categories for browsing and discovery.",
                    children=(
                        template(
                            "Product",
                            purpose="Present an individual fashion product, its details, variants, and purchasing actions.",
                        ),
                    ),
                ),
            ),
        ),
        page(
            "Editorial",
            required=False,
            purpose="Provide a dedicated editorial environment for fashion storytelling and visual content.",
            children=(
                page(
                    "Story",
                    required=False,
                    purpose="Present a narrative or creative story related to the brand, collection, or fashion context.",
                ),
                page(
                    "Campaign",
                    required=False,
                    purpose="Present a campaign and communicate its creative direction and visual identity.",
                ),
                page(
                    "Lookbook",
                    required=False,
                    purpose="Present curated looks and styling combinations from the brand's collections.",
                ),
            ),
        ),
        page(
            "Journal",
            required=False,
            purpose="Publish ongoing editorial content, brand news, fashion perspectives, and cultural stories.",
        ),
        page(
            "About",
            purpose="Explain the fashion brand's identity, heritage, values, and creative positioning.",
            children=(
                page(
                    "Brand",
                    required=False,
                    purpose="Present the brand identity, positioning, and defining characteristics.",
                ),
                page(
                    "Story",
                    required=False,
                    purpose="Explain the history, inspiration, and narrative behind the fashion brand.",
                ),
                page(
                    "Sustainability",
                    required=False,
                    purpose="Communicate the brand's sustainability practices, commitments, and approach.",
                ),
            ),
        ),
        page(
            "Stores",
            required=False,
            purpose="Provide information about physical stores, locations, and shopping experiences.",
        ),
        page(
            "Contact",
            purpose="Provide a direct communication channel for customer, commercial, or brand inquiries.",
        ),
    ),
    single_page_links=(
        LinkRule("Hero", "Collection", LinkType.NAVIGATION),
        LinkRule("Collection", "Featured Products", LinkType.NAVIGATION),
        LinkRule("Featured Products", "Editorial", LinkType.NAVIGATION),
        LinkRule("Editorial", "Story", LinkType.NAVIGATION),
        LinkRule("Story", "Campaign", LinkType.NAVIGATION),
        LinkRule("Campaign", "Lookbook", LinkType.NAVIGATION),
        LinkRule("Lookbook", "Stores", LinkType.NAVIGATION),
        LinkRule("Hero", "Featured Products", LinkType.CTA),
    ),
    multi_page_links=(
        LinkRule("Home", "Collections", LinkType.NAVIGATION),
        LinkRule("Home", "Shop", LinkType.NAVIGATION),
        LinkRule("Home", "Editorial", LinkType.NAVIGATION),
        LinkRule("Home", "Journal", LinkType.NAVIGATION),
        LinkRule("Home", "About", LinkType.NAVIGATION),
        LinkRule("Home", "Stores", LinkType.NAVIGATION),
        LinkRule("Home", "Contact", LinkType.NAVIGATION),
        LinkRule("Collections", "Shop", LinkType.CTA),
        LinkRule("Shop", "Shop.Category.Product", LinkType.NAVIGATION),
        LinkRule("Shop.Category.Product", "Contact", LinkType.CTA),
        LinkRule("Editorial", "Shop", LinkType.CTA),
    ),
)


# ---------------------------------------------------------------------------
# Profile registry
# ---------------------------------------------------------------------------


PROFILES: dict[SiteType, SiteProfile] = {
    site_profile.site_type: site_profile
    for site_profile in (
        LANDING_PAGE,
        SAAS,
        AGENCY,
        PORTFOLIO,
        ECOMMERCE,
        TRAVEL,
        WELLNESS,
        FINTECH,
        TECHNOLOGY,
        FASHION,
    )
}