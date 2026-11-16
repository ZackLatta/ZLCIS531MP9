# MP 9 Annotation Codebook: 8-Class Hip-Hop Trope & Subgenre Ontology

**Track:** VDB Track (CIS 731 Custom PS 6 Ontology)  
**Schema:** `schema/ontology_instances.json` & `ontology.schema.json`  
**Pathway:** Pathway A — Third-Party Ground-Truth Audit  

## 1. Label Definitions, Decision Rules & Labeled Exemplars

### 1. `Hustle_Narrative`
- **Decision Rule:** Economic ascent, street entrepreneurship, financial striving, or hardcore street survival narratives (`Trope:HustleNarrative`; indicators: *grind, corner, out the mud, trapping, stock portfolio, investments*). Assign when economic hustle dominates over geographic pride or institutional critique.
- **Gold Exemplar (`gold_00`):** `Artist: 2nd II None | RYM Genres: Gangsta Rap | Trope Descriptor: Heavy, stripped-down drum machine beats.`

### 2. `Regional_Authenticity`
- **Decision Rule:** Explicit city, borough, or regional rootedness and local scene allegiance (`Trope:RegionalAuthenticity`; indicators: *area code, borough, repping the block, 510, 718, 404, 312*). Assign when place identity or regional scene affiliation is primary without dominant subgenre sonic markers.
- **Gold Exemplar (`gold_01`):** `Artist: 18+ | RYM Genres: Alternative R&B; Hip Hop; UK Bass | Trope Descriptor: Relaxed, dream-like, and reverb-heavy production; heavy Chillwave influence and obscure sample choices.`

### 3. `Lyrical_Sovereignty`
- **Decision Rule:** Technical emcee virtuosity, multi-syllabic internal rhyme density, battle stance, or abstract/experimental wordplay (`Trope:LyricalSovereignty`; indicators: *bars, flow, multi-syllabic, freestyle, cypher*) at standard tempos (`bpm_canonical < 128`).
- **Gold Exemplar (`gold_02`):** `Artist: Adam Vida | RYM Genres: Hip Hop; Nerdcore Hip Hop | Trope Descriptor: Sped-up, high-pitched vocal samples layered over slick, soulful production.`

### 4. `Systemic_Critique`
- **Decision Rule:** Institutional critique, structural inequality, policing/judicial commentary, or socio-political resistance (`Trope:SystemicCritique`; indicators: *redlining, police brutality, prison industrial, gentrification, panther*).
- **Gold Exemplar (`gold_03`):** `Artist: A$AP Twelvyy | RYM Genres: Hardcore Hip Hop | Trope Descriptor: Relaxed, dream-like, and reverb-heavy production; heavy Chillwave influence and obscure sample choices.`

### 5. `Boom_Bap`
- **Decision Rule:** East Coast acoustic kick-snare drum breaks (`85–102 BPM`), unquantized MPC/SP-1200 swing, and filtered jazz/soul loops (`East Coast` subgenre taxonomy).
- **Gold Exemplar (`gold_04`):** `Artist: 2 Chainz | RYM Genres: Drumless; Hip Hop; Jazz Rap; Pop Rap; Trap | Trope Descriptor: Acoustic-sounding drum pattern; characterized by a kick drum on the downbeat followed by a cracking snare on the upbeat.`

### 6. `G_Funk`
- **Decision Rule:** West Coast melodic Moog/sine synthesizers, P-Funk basslines, and laid-back tempo (`80–96 BPM`) (`West Coast` subgenre taxonomy).
- **Gold Exemplar (`gold_05`):** `Artist: 11/5 | RYM Genres: G-Funk; Gangsta Rap | Trope Descriptor: Pounding, menacing sound built on slowed-down Funk samples, live studio instrumentation, and prominent synth basslines.`

### 7. `Trap`
- **Decision Rule:** Southern syncopated 808 sub-bass glides (`sub_bass_ratio >= 0.36`), 32nd-note hi-hat rolls, and dark minor-key loops (`Southern` subgenre taxonomy).
- **Gold Exemplar (`gold_06`):** `Artist: $NOT | RYM Genres: Pop Rap; Trap | Trope Descriptor: Catchy tunes, verse-chorus structures, and melodious vocals.`

### 8. `Chopper`
- **Decision Rule:** Midwest/fast-cadence rapid-fire double/quadruple-time polysyllabic delivery (`bpm_canonical >= 128` or explicit double-time/chopper vocal descriptors) (`Midwest` subgenre taxonomy).
- **Gold Exemplar (`gold_07`):** `Artist: $uicideboy$ | RYM Genres: Cloud Rap; Horrorcore; Trap | Trope Descriptor: Distinctive fast hi-hat sounds and heavy bass set to moderate tempos.`

## 2. Boundary Cases & Adjudication Rules

- **Boundary 1 (`Regional_Authenticity` vs. `G_Funk`):** West Coast or non-specific regional artists lacking explicit P-Funk/sine-wave sonic descriptors adjudicate to `Regional_Authenticity` (e.g., `gold_01`: Annotator 1 `Regional_Authenticity` vs. Annotator 2 `G_Funk` → adjudicated `Regional_Authenticity`).
- **Boundary 2 (`Lyrical_Sovereignty` vs. `Boom_Bap`):** Technical or unconventional emcee passages without explicit acoustic downbeat-kick/upbeat-snare drum-break descriptors adjudicate to `Lyrical_Sovereignty` (e.g., `gold_02`: Annotator 1 `Lyrical_Sovereignty` vs. Annotator 2 `Boom_Bap` → adjudicated `Lyrical_Sovereignty`).
- **Boundary 3 (`Hustle_Narrative` vs. `Systemic_Critique`):** Street/gangsta narratives lacking explicit institutional, judicial, or political critique markers adjudicate to `Hustle_Narrative` (e.g., `gold_08`: Annotator 1 `Hustle_Narrative` vs. Annotator 2 `Systemic_Critique` → adjudicated `Hustle_Narrative`).