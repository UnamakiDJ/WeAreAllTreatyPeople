"""
Core dataclasses for Treaty Bridge Project.
"""

from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Optional
from datetime import datetime


# ---------- People / Figures ----------
@dataclass
class MiKmawFigure:
    name: str
    role: str
    life_dates: str
    bio: str
    significance: str
    key_sources: List[str]
    image_url: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


# ---------- Vocabulary ----------
@dataclass 
class MiKmawWordDialect:
    sf_orthography: Optional[str] = None
    listuguj_orthography: Optional[str] = None
    pronunciation_sfo: Optional[str] = None
    pronunciation_lo: Optional[str] = None
    pronunciation_ipa: Optional[str] = None
    context: str = ""
    two_eyed_seeing: str = ""


@dataclass
class MiKmawWord:
    english: str
    dialects: Dict[str, MiKmawWordDialect]
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


# ---------- History ----------
@dataclass
class HistoryNode:
    id: str
    title: str
    era_label: str
    summary: str
    themes: List[str]
    key_figures: List[str]
    key_sources: List[str]
    notes_for_two_eyed_seeing: str
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


# ---------- Teachings ----------
@dataclass
class SacredTeaching:
    name: str
    animal_symbol: Optional[str]
    description: str
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class SevenGenerationsModel:
    description: str
    past_seven: str
    future_seven: str
    warnings: str
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


# ---------- Kluskap & Science ----------
@dataclass
class ScienceLink:
    field: str
    summary: str
    sources: List[str]
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class KluskapLegend:
    id: str
    title: str
    mikmaw_title_sfo: Optional[str]
    mikmaw_title_lo: Optional[str]
    place_names: List[str]
    summary_english: str
    themes: List[str]
    two_eyed_comment: str
    science_links: List[ScienceLink]
    cultural_sources: List[str]
    notes: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


# ---------- Timeline ----------
@dataclass
class TimelineEvent:
    id: str
    start: Any
    end: Any
    label: str
    era: str
    region: List[str]
    tags: List[str]
    western_lens_summary: str
    western_sources: List[str]
    lnuk_lens_summary: str
    lnuk_sources: List[str]
    two_eyed_seeing: str
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


# ---------- Main Context ----------
@dataclass
class HomeContext:
    figures: Dict[str, MiKmawFigure]
    history_nodes: Dict[str, HistoryNode]
    sacred_teachings: List[SacredTeaching]
    seven_generations: SevenGenerationsModel
    mi_kmaw_words: Dict[str, MiKmawWord]
    kluskap_legends: Dict[str, KluskapLegend]
    timeline_events: List[TimelineEvent]
    main_sources: List[str]
    orthography_options: List[str]
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "figures": {k: v.to_dict() for k, v in self.figures.items()},
            "history_nodes": {k: v.to_dict() for k, v in self.history_nodes.items()},
            "sacred_teachings": [t.to_dict() for t in self.sacred_teachings],
            "seven_generations": self.seven_generations.to_dict(),
            "mi_kmaw_words": {k: v.to_dict() for k, v in self.mi_kmaw_words.items()},
            "kluskap_legends": {k: v.to_dict() for k, v in self.kluskap_legends.items()},
            "timeline_events": [e.to_dict() for e in self.timeline_events],
            "main_sources": self.main_sources,
            "orthography_options": self.orthography_options,
        }
