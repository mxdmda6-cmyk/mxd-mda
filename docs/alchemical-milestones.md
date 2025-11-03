# Alchemical Milestones
## MXD-MDA Sprint Timeline & Phases

*The transmutation of ideas into manifestation follows the alchemical path*

---

## 🗓️ Sprint Overview

Each sprint represents a stage in the alchemical process, with target dates and deliverables. All dates include a ±1 week buffer to accommodate the organic nature of creative and technical work.

---

## 🔥 Sprint 0: Calcination
**Breaking Down the Old - Foundation Phase**

**Duration:** 2 weeks  
**Target Dates:** Week of Nov 4, 2025 - Week of Nov 18, 2025 *(±1 week)*

### Goals
Establish the foundational infrastructure and destroy blockers to rapid development.

### Key Deliverables
- ✅ Repository structure and documentation skeleton
- ✅ CI/CD pipeline for EPUB validation
- ✅ Basic web tools (Story Architect, Production Dashboard)
- ✅ Environment configuration templates
- ✅ Integration guide and production skill documents

### Success Criteria
- [ ] All documentation skeletons in place with TODO markers
- [ ] EPUB validation workflow passing (or skipping if no EPUBs yet)
- [ ] Web tools accessible and demonstrating core UI
- [ ] Team onboarded to alchemical framework

### Risks & Mitigations
- **Risk:** Team unfamiliarity with alchemical framing
  - *Mitigation:* Workshop session to explain 7-stage framework
- **Risk:** Tool complexity (Pandoc, InDesign, EPUBCheck)
  - *Mitigation:* Provide installation guides and Docker option

---

## 🌬️ Sprint 1: Separation
**Isolating Components - Content & Tooling**

**Duration:** 3 weeks  
**Target Dates:** Week of Nov 18, 2025 - Week of Dec 9, 2025 *(±1 week)*

### Goals
Separate content from infrastructure; establish distinct production workflows.

### Key Deliverables
- [ ] Complete Markdown→InDesign conversion script with Pandoc
- [ ] First test chapter drafted and formatted
- [ ] EPUB3 export working with validation passing
- [ ] QR code generation workflow documented
- [ ] FastAPI server scaffolding with Gemini integration

### Success Criteria
- [ ] Test chapter flows through entire pipeline
- [ ] Conversion scripts handle edge cases gracefully
- [ ] EPUB validates without errors in EPUBCheck
- [ ] QR codes generated and tested in print/digital

### Risks & Mitigations
- **Risk:** Pandoc limitations with complex formatting
  - *Mitigation:* Define simplified Markdown subset for MVP
- **Risk:** InDesign automation complexity
  - *Mitigation:* Accept manual steps for MVP, automate later

---

## 🤝 Sprint 2: Conjunction
**Union of Opposites - Integration & AR**

**Duration:** 3 weeks  
**Target Dates:** Week of Dec 9, 2025 - Week of Dec 30, 2025 *(±1 week)*

### Goals
Unite physical and digital experiences through AR markers and AI-powered story generation.

### Key Deliverables
- [ ] AR marker workflow fully operational (QR codes + image recognition)
- [ ] Story Architect connected to FastAPI backend with Gemini API
- [ ] Production Dashboard with live dependency tracking
- [ ] Chapter 1 (Calcination stage) complete and validated
- [ ] Platform content strategy finalized (TikTok, Instagram, Discord)

### Success Criteria
- [ ] QR codes link to working AR experiences
- [ ] Story Architect generates coherent narrative using AI
- [ ] Dashboard visualizes project dependencies and critical path
- [ ] Chapter 1 readable in EPUB format on multiple devices

### Risks & Mitigations
- **Risk:** AR provider API instability
  - *Mitigation:* Build fallback static experiences
- **Risk:** Gemini API rate limits or costs
  - *Mitigation:* Implement caching and request throttling

---

## 🍷 Sprint 3: Fermentation
**Adding Life - Community & Publication**

**Duration:** 4 weeks  
**Target Dates:** Week of Dec 30, 2025 - Week of Jan 27, 2026 *(±1 week)*

### Goals
Bring the project to life with community engagement and initial publication.

### Key Deliverables
- [ ] Chapters 1-3 complete and validated (Calcination, Dissolution, Separation)
- [ ] KDP package ready for Amazon publication
- [ ] Discord community active with role system and engagement rituals
- [ ] TikTok and Instagram content calendar with first posts
- [ ] Analytics integration tracking key metrics
- [ ] Public beta test with early readers

### Success Criteria
- [ ] 3 chapters published and error-free
- [ ] Community of 50+ engaged members on Discord
- [ ] Social media accounts established with 10+ posts
- [ ] Positive feedback from beta readers (survey)
- [ ] Analytics showing engagement with AR experiences

### Risks & Mitigations
- **Risk:** Low community engagement
  - *Mitigation:* Seed community with existing networks, offer incentives
- **Risk:** Publication delays or technical issues
  - *Mitigation:* Test KDP upload process early in sprint

---

## 📊 Cross-Sprint Metrics

### Velocity Tracking
- Story points per sprint (to be baselined in Sprint 0)
- Cycle time from draft to published chapter
- Validation error rate trend

### Quality Gates
- All PRs must pass:
  - ✅ pr-ci check
  - ✅ epub-validation check (if EPUBs present)
  - ✅ Manual code review
  - ✅ Documentation updated

### Team Capacity
- TODO: Define team size and availability
- TODO: Identify key roles (writers, designers, developers, marketers)
- TODO: Plan for holidays and time off (Dec/Jan period)

---

## 🔮 Post-MVP Phases (Future Sprints)

### Sprint 4: Distillation
**Refining the Experience**
- Polish based on beta feedback
- Performance optimization
- Advanced AR experiences

### Sprint 5: Coagulation
**Solidifying the Product**
- Full publication (all 7 chapters)
- Marketing campaign launch
- Revenue tracking and optimization

---

## 📅 Key Dates Quick Reference

| Milestone | Target Start | Target End | Buffer |
|-----------|-------------|------------|--------|
| Sprint 0: Calcination | Nov 4, 2025 | Nov 18, 2025 | ±1 week |
| Sprint 1: Separation | Nov 18, 2025 | Dec 9, 2025 | ±1 week |
| Sprint 2: Conjunction | Dec 9, 2025 | Dec 30, 2025 | ±1 week |
| Sprint 3: Fermentation | Dec 30, 2025 | Jan 27, 2026 | ±1 week |

---

## 🔄 Sprint Review & Retrospective Cadence

- **Sprint Planning:** First Monday of each sprint
- **Daily Stand-ups:** Async check-ins via Discord
- **Sprint Review:** Last Friday of each sprint (demo to stakeholders)
- **Sprint Retrospective:** Last Friday of each sprint (team only, after review)

---

## 📖 Document Status

**Current Version:** 1.0 - MVP Foundation  
**Last Updated:** 2025-11-03  
**Status:** 🚧 Living Document - Updated at end of each sprint

**Next Review:** End of Sprint 0 (Week of Nov 18, 2025)

---

*"The alchemical work is never rushed, yet never stagnant. Each phase unfolds in its own time, transmuting base materials into gold."*
