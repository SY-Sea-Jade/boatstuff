---
name: my-boat
description: "Reference profile for Sea Jade, my Bavaria Cruiser 36 (Farr, 2011). Use this skill proactively whenever asked about sailing, seamanship, navigation, anchoring, passage planning, boat maintenance, engine servicing, electrical systems, antifouling, rigging, safety equipment, provisioning, Scottish waters, or anything boat-related — even if the question seems generic. Always tailor advice to this specific vessel, her systems, and the waters she sails. Trigger on keywords: boat, sail, engine, anchor, marina, passage, tidal, VHF, chart, foul, keel, antifoul, chandlery, bilge, diesel, mast, furler, winch, halyard, sheet, preventer, reefing, Bavaria, Volvo, D1-30, bow thruster, Garmin, AIS, Clyde, Hebrides, Scotland, west coast, corrosion, zinc, anode."
---

# My Boat — Bavaria Cruiser 36 (2011)

## Vessel Summary

| Field         | Detail                                             |
|---------------|----------------------------------------------------|
| Make / Model  | Bavaria Cruiser 36                                 |
| Year Built    | 2011                                               |
| Designer      | Bruce Farr                                         |
| Launched      | June 2012                                          |
| Home Base     | Largs Yacht Haven                                  |
| LOA           | 11.3 m                                             |
| LWL           | 9.9 m                                              |
| Beam          | 3.67 m                                             |
| Draft         | 1.97 m (fin keel)                                  |
| Ballast       | 2080 kg                                            |
| Displacement  | 7000 kg, cast iron keel                            |
| Hull          | GRP (white topsides)                               |
| Diesel Tank   | 151 l                                              |
| Water Tanks   | 208 l and 150 l                                    |
| Holding Tank  | 70l                                                |
| Bow Anchor    | Rocna Mk1 15 kg with 60m chain rode                |
| Kedge Anchor  | Fortress Guardian 5.5kg anchor, 5m chain, 50m rode | 
| Swim Platform | Hinged at transom, 450kg max load                  |
| Rig           | Fractional sloop, furling headsail, in-mast furling mainsail (standard BC36 fit) |
| Sailboat Data | https://sailboatdata.com/sailboat/bavaria-cruiser-36-farr/ |

## Engine — Volvo Penta D1-30F

- **Type**: 3-cylinder, 4-stroke diesel, 28 hp, MDI and starter replaced June 2026
- **Saildrive**: MS130 saildrive unit (key galvanic corrosion risk area — see below)
- **Raw water cooling**: seawater pump drives impeller; check/replace impeller annually or every 200 hrs
- **Heat exchanger**: freshwater-cooled block with raw water exchanger
- **Fuel system**: Racor 500 primary fuel filter + engine-mounted secondary filter; bleed sequence: secondary filter → fuel pump → injectors
- **Oil**: 15W-40 marine diesel, sump ~3.5 L; change every 100–150 hrs or annually
- **Exhaust** Replacement stainless manifold with NASA EX-1 exhaust temperature probe and display with alarm at companionway
- **Propeller**: 2-blade, fixed alloy prop, fitted 2022
- **Belts**: single serpentine-style belt drives alternator and raw water pump; check tension and cracking annually
- **Zincs**: saildrive anode (aluminium collar + propeller anode) — inspect every haul-out, replace if >50% consumed
- **NMEA**  Yacht Devices YDEG-04 NMEA 2000 engine gateway connected via CANBus y-adapter from tachometer
- **Common faults**: injector seal weeping (smell of diesel in bilge), raw water impeller failure (rising temp alarm), air in fuel after filter change (requires bleed)

## Electrical & Battery

- **Charging**: 
  - High output 110A replacement engine alternator fitted 2020-2024
    - Original factory fit alternator held as spare
    - Pink wire for voltage drop detection wired back to house bank
  - Victron ARGOFET battery isolator, 3 output, 100A, fitted 2024
- **Solar Panels** 
  - 2xVictron SPM041401200 140w solid panels wired in parallel
  - Victron MPPT 100/20 charger
- **Battery bank**: 
  - 2@ Exide EP1200 AGM house bank replaced April 2026
  - 1 @ AQU100MF Aquaflex Marine Battery 12V 80Ah(C5) start battery,
  - 1 @ spare Banner 105Ah start battery
  - 1 95Ah bow thruster battery
  - Batteries, chargers, main fuses, NMEA2000 power feed under and behind port side saloon sofa
- **Monitoring**: Renogy shunts and battery monitors for house and starter
- **Shore power**: 230 V shore power (standard BC36 fit)
- **Galvanic isolator**: SafeSure GI-100-SM fitted in shore power earth line
- **Earthing**: common earth below starboard aft cabin, thru-hull to a mushroom zinc anode
- **Battery Charger**: Quick SBC NRG 230VAC – 12VDC, 45amp
- **Distribution**
  - AC Shore power 
    - 16A socket at swim platform
    - Master control in transom void
    - Directly wired to Baumatic microwave at galley and calorifier under stardboard aft cabin
    - Bavaria Shore Power Control Panel
      - Master RCD - Sursum RCCB RP2203 with test switch, to be tested every 6 months
      - 3 Sursum B16 S1 RCDs for hot water, sockets/microwave/charger and heads socket
      - Reverse polarity detection with light
    - UK 13A sockets
      - Single, port side, forepeak cabin
      - Single, starboard aft cabin
      - Double, starboard saloon floor level
      - Double with USB-A outlets, starboard saloon behind sofa
      - Single, heads locker (on its own RCD)
    - Continental 13A sockets
      - Single, behind cooker
      - Single, integrated into shore power control panel
    - 4-way 13 amp strip behind cooker connected by plug to Bluetti AC outlet
  - DC
    - Control panel - Bavaria Main Panel 301
      - Switches for all DC systems
      - F1-F5 additional buttons
      - F1 TV, F2 Cockpit Lights, F3 may have been alternative diesel heater control
      - Anchor relay behind panel
      - Cigar lighter type outlet on control panel
      - Wiring back from tank senders to panel
    - Primary fuses on bulkhead at battery bay
      - 125A and 63A NH00 Mersen 
    - DC fuse / distribution box under starboard aft bunk
      - Unattached on block of wood
      - Blade fuses
      - Known lines out to xpeedingrods diesel heater and RUT956 modem, possibly also to transom void lighting
    - Known dead wiring
      - Webasto wiring from DC panel to transom void
    - Known direct house bank wiring
      - NASA Gas monitor, fitted 2026
      - Seaflo automatic bilge control/float/pump
    - Known direct engine bank wiring
      - Engine bay light

- **Bow thruster**: 
  - Sleipner Sidepower SE60/185S
  - Dedicated thruster battery
  - BEP Marine 125A VSR installed at battery bay to charge from house bank
  - Brushes and seals require inspection at haul-out
- **Power Station**: Bluetti Elite 100 V2, with diverter switch for solar panels
- **Lighting**
  - LED ceiling lights in saloon, switch at companion way
  - LED ceiling lights in heads, switch at companion way
  - LED downlighters in saloon, switch at companion way and forward bulkhead
  - LED downlighters in forepeak and starboard aft cabin, switched in each cabin
  - LED spotlights, G4 bulbs, in saloon, forepeak, starboard aft cabin
  - Chart table spotlight, LED bulb
  - 2 LED workshop panels in transom void, 1 in engine bay
  - LED floor level cockpit lights
  - Bow, stern navigation lights, masthead anchor light, steaming light on mast, cockpit floodlight (not working) on mast, switched on main DC panel. 

## Navigation & Electronics

- **Chartplotter**: 
  - Garmin GPSMAP 4010 (10.4" colour, older unit)
  - Chart source: VEU706L UK-Ireland-The Netherlands v2021 v22.00
- **AIS**: 
  - Transponder fitted (Class B - Garmin AIS600 transceive)
     - connect to chartplotter via NMEA2000 for target overlay
  - RUT956 modem broadcasts own position to AISHub, MarineTraffic and VesselFinder when SignalK down
  - SignalK server sends own position and AIS transceiver targets to AISHub, MarineTraffic and VesselFinder
- **VHF**: Raymarine 55E, MMSI 235094115. Cobra handheld VHF with GPS and DSC - MMSI 235934885.
- **Beacons**: SMRT Alert AIS Beacon for Wendy. McMurdo Fastfind Return Link PLB, registered as NKZ87YW, for Jey or mounted at companionway as boat beacon.
- **Radar**: Garmin Digital HD GMR18HD, STP wiring back to plotter
- **GPS**: GPS24x-NMEA2000, installed Jan 2026. Spare GPS21x-NMEA2000
- **Autopilot**: GHC10 head unit, Garmin GHP12 control unit, Lewmar linear drive unit
- **Instruments**: ST60+ wind/depth/speed instruments, connected to NMEA 2000 by ShipModul MiniPlex-3E-N2K, with LAN cable to bridge NMEA to Ethernet via RUT956.
- **Bus**: NMEA 2000 bus from port-side saloon to across rear bulkhead. NMEA 0183 only for plotter to/from Raymarine VHF. Originally with a Raymarine E85001 box to interface ST60+ instruments to plotter via NMEA0183, now replaced with ShipModul interface.
- **Internet**: 
 - Starlink Mini, mounted as needed, hard-wired LAN to RUT956 and USB-C to Bluetti for power. 
 - Teltonika RUT956 mounted in stern compartment and permanently connected, ID Mobile 4G unlimited data SIM and Wireguard peering back to home network, and Modbus exposure of LTE and GPS stats for SignalK. - 
- **Server**: 
  - NanoPi M5 with 64GB UFS, requires 6-20V, powered off USB-C port on Bluetti.
  - Running SignalK to redistribute data for SavvyNavvy and AngelNav, run anchor alarm, paint eInk displays and log NMEA0183 to disk and core data to Parquet, backed up to a Garage S3 server at home. Also exposed via WilhelmSK on iPhone and iPad. 

## Rigging
- **Foresail**: Selden Furlex 200S roller reefing
- **Mainsail**: Fully battened, slab reefing Dacron, mid-boom mainsheet with German system, gas rod kicker, lazyjacks and stackpack
- **Stays**: Block and tackle back stay adjuster
- **Pole**: Forespar telescopic whisker pole
- **Rudder**: Spade, Jefa, rebuilt June 2026

## Sailing Area

- **Primary**: Scottish west coast and Hebrides — Firth of Clyde, Kintyre, Islay, Jura, Colonsay, Mull, Ardnamurchan, Small Isles, Outer Hebrides
- **General**: coastal cruising, not offshore/ocean passages
- **Tidal considerations**: significant tidal streams in Scottish waters — Sound of Luing, Dorus Mòr, Corryvreckan vicinity, Kyle of Lochalsh; always consult Reeds Almanac or CCC Sailing Directions
- **Weather**: Atlantic depressions move through quickly; forecasts from Met Office Inshore Waters, Windy, or PredictWind; VHF weather broadcasts on ch 23/84 from Coastguard

## Known Issues & Maintenance Focus Areas

### Galvanic Corrosion (Active Concern)
- Saildrive units on Bavaria 36s are a known vulnerability for galvanic and electrolytic corrosion
- Check: saildrive leg aluminium casing for pitting, saildrive bellows condition (replace every 5–7 years regardless of appearance), propeller shaft seal
- Mitigation: maintain saildrive anode, isolate shore power properly (use galvanic isolator or isolation transformer), check marina wiring quality
- At haul-out: inspect saildrive carefully before antifouling; photograph baseline

### General Maintenance Priorities
- **Antifouling**: annual haul-out typical for Scottish waters (heavy fouling season); use hard antifoul suitable for Clyde/west coast. International Cruiser 250 on hull and International Trilux on propeller, saildrive leg and bow thruster blades
- **Seacocks**: grease and exercise all seacocks annually; DZR replaced in 2015
- **Rigging**: inspect standing rigging (swageless or swaged terminals) annually; check furler bearings and foil joints; in-mast furling manual drum
- **Sails**: UV strip on furling headsail; in-mast mainsail — check sail slug condition and furling drum
- **Bilge**: Seaflo automatic bilge pump and manual bilge pump

## Advice Defaults

When giving advice for this boat:
- **Assume Scottish tidal waters** unless stated otherwise — always flag tidal stream hazards
- **Assume a shorthanded crew** (skipper + wife) — prefer conservative sail plans, easy reefing, roller furling use
- **Engine servicing**: reference D1-30F specifics, not generic diesel advice
- **Galvanic corrosion**: flag any advice that touches shore power, metal underwater fittings, or marina berths
- **Charts/navigation**: Garmin GPSMAP 4010 is the primary plotter; advice should be compatible with that unit's capabilities and age
- **Anchoring**: Interested in Hebridean anchorages — consider holding ground, swell exposure, and emergency egress