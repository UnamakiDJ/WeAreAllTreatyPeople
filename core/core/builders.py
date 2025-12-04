"""
Treaty Bridge Data Module
-------------------------
A Two-Eyed Seeing framework for Mi'kmaw knowledge
Copyright (c) 2025 Treaty Bridge Project

Built with respect for Mi'kmaw Elders, language keepers, and communities.
This is a work-in-progress - always verify with living knowledge sources.
"""

from typing import Dict, List
from .dataclasses import *
"""
Builder functions for creating Treaty Bridge data.
"""

from typing import Dict, List
from .dataclasses import *


# ============ FIGURE BUILDERS ============
def build_core_figures() -> Dict[str, MiKmawFigure]:
    """Build the core figures database."""
    figures = {}
    
    figures["membertou"] = MiKmawFigure(
        name="Grand Chief Membertou (Henri Membertou)",
        role="Grand Chief (Saqmaw), political and spiritual leader",
        life_dates="c.1507–1611",
        bio="Grand Chief of the Mi'kmaq near Port Royal in the early 1600s...",
        significance="Embodies early Mi'kmaw–French diplomacy...",
        key_sources=[
            "Dictionary of Canadian Biography – Membertou",
            "Daniel N. Paul, We Were Not the Savages",
        ],
        image_url="images/membertou.jpg"
    )
    
    figures["donald_marshall_jr"] = MiKmawFigure(
        name="Donald Marshall Jr.",
        role="Fisher, Treaty Rights Defender, Catalyst for Legal Change",
        life_dates="1953–2009",
        bio="Mi'kmaw man from Membertou who was wrongfully convicted...",
        significance="A symbol of both the violence of colonial law...",
        key_sources=[
            "R. v. Marshall (1999), Supreme Court of Canada",
            "Royal Commission on the Donald Marshall Jr. Prosecution",
        ],
        image_url="images/donald_marshall.jpg"
    )
    
    # Add more figures as needed...
    
    return figures


# ============ WORD BUILDERS ============
def build_core_words() -> Dict[str, MiKmawWord]:
    """Build the core vocabulary database."""
    words = {}
    
    words["tupsi"] = MiKmawWord(
        english="alder tree",
        dialects={
            "default": MiKmawWordDialect(
                sf_orthography="tupsi",
                listuguj_orthography="tupsi",
                pronunciation_sfo="TUP-sih",
                pronunciation_lo="TUP-see",
                context="Alder tree, important in riparian zones...",
                two_eyed_seeing="Relational being in the riverbank ecosystem..."
            )
        }
    )
    
    words["gesig/kesik"] = MiKmawWord(
        english="winter / it is winter",
        dialects={
            "default": MiKmawWordDialect(
                sf_orthography="gesig",
                listuguj_orthography="kesik",
                pronunciation_sfo="GEH-sik",
                pronunciation_lo="KEH-sik",
                context="Refers to winter season...",
                two_eyed_seeing="Winter as rest and reflection..."
            )
        }
    )
    
    return words


# ============ TEACHING BUILDERS ============
def build_sacred_teachings() -> List[SacredTeaching]:
    """Build the Seven Sacred Teachings."""
    return [
        SacredTeaching(name="Wisdom", animal_symbol="Beaver", 
                      description="Using knowledge for the good of all relations."),
        SacredTeaching(name="Love", animal_symbol="Eagle",
                      description="Caring deeply for all beings and yourself."),
        # ... add all 7
    ]


def build_seven_generations_model() -> SevenGenerationsModel:
    """Build the Seven Generations model."""
    return SevenGenerationsModel(
        description="Seven Generations thinking links the past seven generations...",
        past_seven="Ancestors hold and transmit knowledge...",
        future_seven="Your actions today ripple forward...",
        warnings="Greed can appear in many forms..."
    )


# ============ KLUSKAP BUILDERS ============
def build_kluskap_legends() -> Dict[str, KluskapLegend]:
    """Build Kluskap legends with science links."""
    legends = {}
    
    legends["creation_kluskap_mikmaq"] = KluskapLegend(
        id="creation_kluskap_mikmaq",
        title="The Creation of Kluskap and the Mi'kmaq",
        place_names=["Cape Blomidon", "Bay of Fundy", "Mi'kma'ki"],
        summary_english="Lightning strikes the earth and Kluskap is formed...",
        themes=["creation", "ice", "landform", "ancestors"],
        two_eyed_comment="From a Mi'kmaw eye, this is a sacred origin story...",
        science_links=[
            ScienceLink(
                field="Geology / Glaciology",
                summary="Glacial ice covered Mi'kma'ki until roughly 13,000–11,000 years ago...",
                sources=["Quaternary geology of Atlantic Canada"]
            )
        ],
        cultural_sources=[
            "Mi'kmawey Debert Cultural Centre",
            "Whitehead, Stories from the Six Worlds"
        ]
    )
    
    # Add more legends...
    
    return legends


# ============ HISTORY BUILDERS ============
def build_history_nodes() -> Dict[str, HistoryNode]:
    """Build history nodes for deep dives."""
    nodes = {}
    
    nodes["membertou_relocation"] = HistoryNode(
        id="membertou_relocation",
        title="Relocation of Membertou Community from King's Road",
        era_label="20th Century Displacement & Resilience",
        summary="In the early 20th century, the Mi'kmaw community...",
        themes=["displacement", "urbanization", "colonial policy"],
        key_figures=[],
        key_sources=["Membertou Heritage Park archives"],
        notes_for_two_eyed_seeing="Municipal and federal governments framed the move..."
    )
    
    return nodes


# ============ TIMELINE BUILDERS ============
def build_timeline_events() -> List[TimelineEvent]:
    """Build the Two-Eyed Seeing timeline."""
    events = []
    
    # Deglaciation
    events.append(TimelineEvent(
        id="deglaciation",
        start="-12000 BP",
        end="-9000 BP",
        label="Ice Leaves, Land Rises",
        era="Deep Time & Creation",
        region=["All Mi'kma'ki"],
        tags=["geology", "ice age", "creation"],
        western_lens_summary="Retreat of the Laurentide Ice Sheet...",
        western_sources=["Quaternary geology of Atlantic Canada"],
        lnuk_lens_summary="Stories of a world of ice and water changing...",
        lnuk_sources=["Mi'kmawey Debert – creation narratives"],
        two_eyed_seeing="Both lenses describe Mi'kma'ki in motion..."
    ))
    
    # Add all your other timeline events...
    # Marshall Decision, Elsipogtog, Sipekne'katik, etc.
    
    return events


# ============ MAIN BUILDER ============
def build_home_context() -> HomeContext:
    """Build the complete HomeContext with all data."""
    figures = build_core_figures()
    words = build_core_words()
    sacred = build_sacred_teachings()
    seven_gen = build_seven_generations_model()
    legends = build_kluskap_legends()
    timeline = build_timeline_events()
    history_nodes = build_history_nodes()
    
    main_sources = [
        "Daniel N. Paul – We Were Not the Savages",
        "William Wicken – Mi'kmaq Treaties on Trial",
        # ... all your sources
    ]
    
    orthography_options = [
        "Smith/Francis Orthography (S/F.O)",
        "Listuguj Orthography (L.O)"
    ]
    
    return HomeContext(
        figures=figures,
        history_nodes=history_nodes,
        sacred_teachings=sacred,
        seven_generations=seven_gen,
        mi_kmaw_words=words,
        kluskap_legends=legends,
        timeline_events=timeline,
        main_sources=main_sources,
        orthography_options=orthography_options
    )
