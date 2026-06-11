# Literature Map

## Scope
- Landscape sweep entries: 1000
- Serious skim set: 300
- Deep-read set: 240
- Hostile prior-work set: 100
- Field box after sweep: robot manipulation/control robustness under nonideal actuation, especially where contact or IK branch choices interact with signed actuator limits.

## Venue/Source Concentration
- unknown: 111
- arXiv (Cornell University): 88
- IEEE Access: 70
- IEEE Robotics and Automation Letters: 39
- IEEE Transactions on Robotics: 30
- Frontiers in Robotics and AI: 30
- Sensors: 29
- Nature Communications: 22
- ArXiv.org: 19
- Robotics: 17
- Advanced Intelligent Systems: 16
- Applied Sciences: 15
- Frontiers in Neurorobotics: 13
- Advanced Materials: 12
- IEEE/ASME Transactions on Mechatronics: 12

## Year Concentration
- 2023: 166
- 2021: 118
- 2024: 108
- 2020: 104
- 2022: 97
- 2018: 69
- 2019: 68
- 2025: 47
- 2017: 38
- 2016: 34
- 2026: 24
- 2015: 18
- 2013: 17
- 2014: 16
- 2011: 10

## Mechanism Families Observed
- Fault-tolerant and adaptive robot control: strong on diagnosis/reconfiguration, weak on pre-fault sign-asymmetric policy structure.
- Saturation-aware constrained control: strong on feasibility projection, often assumes symmetric boxes or fixed task/action bases.
- Sim-to-real and dynamics randomization: strong on aggregate mismatch, weak on action representations that expose positive/negative actuator channels.
- Contact and nonprehensile manipulation: strong on object-side motion cones, usually treats robot actuation as a realizability detail.
- Impedance/force control: strong on contact stability, weak on directional authority margins for corrective actions.

## Twenty-Four Hidden Assumptions Worth Breaking
1. Positive and negative authority of a joint are interchangeable up to one scalar limit.
2. A controller can treat actuator mismatch as additive or multiplicative noise without changing the action basis.
3. A manipulation policy should choose contact mode before checking signed actuator feasibility.
4. If a desired end-effector velocity is geometrically feasible, the robot can realize it equally well from all IK branches.
5. Actuator degradation is a rare fault event rather than a persistent directional property.
6. Robustness can be recovered by shrinking a symmetric action set.
7. Domain randomization over scalar gains covers sign-dependent weakness.
8. A learned policy will discover actuator-direction structure without being given signed channels.
9. Contact stability depends mainly on object mechanics, not on direction-specific corrective authority.
10. Operational-space commands are a neutral interface between policy and hardware.
11. Torque saturation only matters near global magnitude limits.
12. Safety filters can project onto symmetric command boxes without changing task-level behavior.
13. The same compliance setting is appropriate for a weak push direction and its strong reverse direction.
14. The low-level servo hides actuator dynamics from manipulation planning.
15. Nullspace or branch choices are secondary comfort choices rather than robustness-critical variables.
16. Actuator calibration errors are small enough to be absorbed by feedback.
17. Contact-rich failures are dominated by perception/contact uncertainty rather than actuation asymmetry.
18. Fault-tolerant control begins after a fault classifier is confident.
19. Action penalties should be even functions of command magnitude.
20. Benchmark success averages reveal directional brittleness.
21. Manipulation primitives can be compared without actuator-side feasibility certificates.
22. Object-level motion cones are sufficient; robot-side signed actuation cones can be ignored.
23. A controller that tracks commands well under symmetric tests will degrade gracefully under asymmetric tests.
24. The actuation model is a property of hardware only, not of the policy representation.

## Candidate Paper Directions
### Signed actuation cone policies
- Broken assumption: Action spaces are symmetric command vectors.
- Mechanism: Represent each joint or actuator as positive and negative nonnegative channels, then select manipulation primitives by projected object-motion feasibility inside the signed cone.
- Strength: It changes the central mechanism: primitive choice is made in actuator-feasibility coordinates rather than in object geometry alone.

### Asymmetry-aware contact-mode planning
- Broken assumption: Contact modes can be ranked before robot-side actuation is considered.
- Mechanism: Attach a directional actuator margin certificate to each contact mode and prune modes whose corrective direction is weak.
- Strength: Strong for planning, but weaker as a standalone paper unless paired with a general action representation.

### Directional compliance scheduling
- Broken assumption: Impedance gains should be symmetric around the nominal trajectory.
- Mechanism: Use signed actuator margins to lower stiffness in weak recovery directions and raise it in strong arrest directions.
- Strength: Practical, but it risks looking like gain scheduling unless the signed feasibility layer is the main object.

### Asymmetry diagnosis from manipulation residuals
- Broken assumption: Actuator faults must be diagnosed by a separate residual observer before policy changes.
- Mechanism: Infer signed actuation cones from task residuals and change primitives online.
- Strength: Useful extension, but identification alone is less central than policy structure.

### Directional benchmark suite
- Broken assumption: Average perturbation benchmarks expose actuator brittleness.
- Mechanism: Evaluate policies over sign-specific action sectors and contact branches.
- Strength: Valuable artifact, but forbidden as benchmark-only without a new mechanism.

## Decision From the Sweep
The strongest direction is **signed actuation cone policies**. It is not a bigger model, a benchmark-only move, uncertainty wrapper, verifier, active learner, or RL variant. It changes the central action mechanism: object-level commands and contact/IK primitive choices are evaluated through sign-specific actuator cones before execution.

## Representative Deep-Read Entries
### 1. Adaptive PID-like fault-tolerant control for robot manipulators with given performance specifications (2018) -- Ye Cao; Yongduan Song
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- Makes less novel: General claim that actuator nonidealities matter for robot control.
- Leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

### 2. Dual arm coordination of redundant space manipulators mounted on a spacecraft (2023) -- S. Kalaycioglu; Anton de Ruiter
- Problem claimed: Control manipulators while respecting torque, velocity, or input constraints.
- Mechanism introduced: Constrained optimization, model predictive control, anti-windup, or control allocation.
- Hidden assumptions: Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate.
- Variables fixed: Actuator coordinates, contact primitive set, and sign-specific effort margins.
- Failure modes ignored: Directional limits that make one branch/contact primitive safer than another for the same object motion.
- Makes less novel: Novelty of merely adding actuator limits to a controller.
- Leaves open: A policy representation where signed actuation cones choose the manipulation primitive itself.

### 3. Neural Networks-Based Fault Tolerant Control of a Robot via Fast Terminal Sliding Mode (2019) -- Shuang Zhang; Pengxin Yang; Linghuan Kong; Wenshi Chen; Qiang Fu; Kaixiang Peng
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- Makes less novel: General claim that actuator nonidealities matter for robot control.
- Leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

### 4. The Control Handbook (2005) -- William S. Levine
- Problem claimed: Control manipulators while respecting torque, velocity, or input constraints.
- Mechanism introduced: Constrained optimization, model predictive control, anti-windup, or control allocation.
- Hidden assumptions: Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate.
- Variables fixed: Actuator coordinates, contact primitive set, and sign-specific effort margins.
- Failure modes ignored: Directional limits that make one branch/contact primitive safer than another for the same object motion.
- Makes less novel: Novelty of merely adding actuator limits to a controller.
- Leaves open: A policy representation where signed actuation cones choose the manipulation primitive itself.

### 5. Finite-Time Adaptive Fault-Tolerant Control for Robot Manipulators With Guaranteed Transient Performance (2025) -- Yongling Xia; Yeqing Yuan; Weichao Sun
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- Makes less novel: General claim that actuator nonidealities matter for robot control.
- Leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

### 6. Adaptive fault tolerant control for a class of input and state constrained MIMO nonlinear systems (2015) -- Xu Jin
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- Makes less novel: General claim that actuator nonidealities matter for robot control.
- Leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

### 7. Control of robot manipulators with consideration of actuator performance degradation and failures (2002) -- Guangjun Liu
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- Makes less novel: General claim that actuator nonidealities matter for robot control.
- Leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

### 8. Highly‐Aligned All‐Fiber Actuator with Asymmetric Photothermal‐Humidity Response and Autonomous Perceptivity (2024) -- Yufan Zhang; Xinran Zhou; Luyun Liu; Shuang Wang; Yue Zhang; Mengjie Wu; et al.
- Problem claimed: Improve robot control, planning, or modeling under physical uncertainty.
- Mechanism introduced: Model-based control, planning, estimation, or learning depending on the paper.
- Hidden assumptions: Actuator authority is either nominal, symmetric, or hidden inside an uncertainty set.
- Variables fixed: Task action basis, actuator sign geometry, and controller-policy boundary.
- Failure modes ignored: Direction-specific action feasibility and its effect on manipulation primitive choice.
- Makes less novel: Broad claim that robustness is important.
- Leaves open: Explicit actuator-asymmetry structure inside the manipulation policy.

### 9. Advanced Control Strategies for Space Systems: Integration of Model Predictive Control and Neural Networks (2025) -- Sean Kalaycioglu; Anton de Ruiter
- Problem claimed: Control manipulators while respecting torque, velocity, or input constraints.
- Mechanism introduced: Constrained optimization, model predictive control, anti-windup, or control allocation.
- Hidden assumptions: Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate.
- Variables fixed: Actuator coordinates, contact primitive set, and sign-specific effort margins.
- Failure modes ignored: Directional limits that make one branch/contact primitive safer than another for the same object motion.
- Makes less novel: Novelty of merely adding actuator limits to a controller.
- Leaves open: A policy representation where signed actuation cones choose the manipulation primitive itself.

### 10. Finite‐time fault‐tolerant adaptive robust control for a class of uncertain non‐linear systems with saturation constraints using integral backstepping approach (2018) -- Seyed Majid Smaeilzadeh; Mehdi Golestani
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- Makes less novel: General claim that actuator nonidealities matter for robot control.
- Leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

### 11. Fuzzy Disturbance Observers-Based Adaptive Fault-Tolerant Control for an Uncertain Constrained Automatic Flexible Robotic Manipulator (2023) -- Yong Ren; Yaobin Sun; Lei Liu
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- Makes less novel: General claim that actuator nonidealities matter for robot control.
- Leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

### 12. Fault-tolerant scheme for robotic manipulator—Nonlinear robust back-stepping control with friction compensation (2021) -- Khurram Ali; Adeel Mehmood; Jamshed Iqbal
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- Makes less novel: General claim that actuator nonidealities matter for robot control.
- Leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

### 13. Robust Adaptive Fuzzy Fault Tolerant Control of Robot Manipulators With Unknown Parameters (2023) -- Shoulin Xu; Bin He
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- Makes less novel: General claim that actuator nonidealities matter for robot control.
- Leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

### 14. Fixed-Time Fuzzy Resilient Consensus Tracking of Nonlinear MASs Under DoS Attacks and Actuator Faults (2024) -- Bo Xu; Yuan‐Xin Li; Zhongsheng Hou
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- Makes less novel: General claim that actuator nonidealities matter for robot control.
- Leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

### 15. First-Principles Models and Safety-Driven Planning for Soft and Rigid Robots (2025) -- Zachary Brei
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- Makes less novel: General claim that actuator nonidealities matter for robot control.
- Leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

### 16. Disturbance Observer-Based Fault-Tolerant Control for Robotic Systems With Guaranteed Prescribed Performance (2020) -- Haifeng Huang; Wei He; Jiashu Li; Bin Xu; Chenguang Yang; Weicun Zhang
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- Makes less novel: General claim that actuator nonidealities matter for robot control.
- Leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

### 17. Fault-tolerant control strategies for industrial robots: state of the art and future perspective on AI-based fault management (2025) -- Zeashan Hameed Khan; Ali A. Nasir; Samir Mekid
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- Makes less novel: General claim that actuator nonidealities matter for robot control.
- Leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

### 18. Push, Press, Slide: Mode-Aware Planar Contact Manipulation via Reduced-Order Models (2026) -- Melih Özcan; Orguner, Umut; Oguz, Ozgur S.
- Problem claimed: Plan and control object motion through intermittent or sticking contact.
- Mechanism introduced: Quasi-static pushing models, motion cones, contact-mode planning, or learned push dynamics.
- Hidden assumptions: The robot can realize planned pusher motions equally well in each direction.
- Variables fixed: The robot-side actuator cone behind the contact-mode model.
- Failure modes ignored: A push mode may be geometrically valid but actuator-directionally brittle.
- Makes less novel: Novelty of contact-mode or pushing mechanics alone.
- Leaves open: Jointly selecting contact/IK primitive and signed actuator cone feasibility.

### 19. Indirect Adaptive Robust Control of Hydraulic Manipulators With Accurate Parameter Estimates (2010) -- Amit Mohanty; Bin Yao
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- Makes less novel: General claim that actuator nonidealities matter for robot control.
- Leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

### 20. Adaptive Fault Tolerant Non-Singular Sliding Mode Control for Robotic Manipulators Based on Fixed-Time Control Law (2022) -- Saim Ahmed; Ahmad Taher Azar; Mohamed Tounsi
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- Makes less novel: General claim that actuator nonidealities matter for robot control.
- Leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

### 21. A Dynamic Programming Framework for Optimal Planning of Redundant Robots Along Prescribed Paths With Kineto-Dynamic Constraints (2023) -- Enrico Ferrentino; Heitor J. Savino; Antonio Franchi; Pasquale Chiacchio
- Problem claimed: Control manipulators while respecting torque, velocity, or input constraints.
- Mechanism introduced: Constrained optimization, model predictive control, anti-windup, or control allocation.
- Hidden assumptions: Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate.
- Variables fixed: Actuator coordinates, contact primitive set, and sign-specific effort margins.
- Failure modes ignored: Directional limits that make one branch/contact primitive safer than another for the same object motion.
- Makes less novel: Novelty of merely adding actuator limits to a controller.
- Leaves open: A policy representation where signed actuation cones choose the manipulation primitive itself.

### 22. Coupling Magnetic Torque and Force for Colloidal Microbot Assembly and Manipulation (2023) -- Coy J. Zimmermann; Andrew J. Petruska; Keith B. Neeves; David W. M. Marr
- Problem claimed: Improve robot control, planning, or modeling under physical uncertainty.
- Mechanism introduced: Model-based control, planning, estimation, or learning depending on the paper.
- Hidden assumptions: Actuator authority is either nominal, symmetric, or hidden inside an uncertainty set.
- Variables fixed: Task action basis, actuator sign geometry, and controller-policy boundary.
- Failure modes ignored: Direction-specific action feasibility and its effect on manipulation primitive choice.
- Makes less novel: Broad claim that robustness is important.
- Leaves open: Explicit actuator-asymmetry structure inside the manipulation policy.

### 23. Fault detection and robust fault recovery control for robot manipulators with actuator failures (2003) -- Jin-Ho Shin; Ju-Jang Lee
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- Makes less novel: General claim that actuator nonidealities matter for robot control.
- Leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

### 24. Active Fault-Tolerant Control Design for Actuator Fault Mitigation in Robotic Manipulators (2021) -- Yashar Shabbouei Hagh; Reza Mohammadi Asl; Afef Fekih; Huapeng Wu; Heikki Handroos
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- Makes less novel: General claim that actuator nonidealities matter for robot control.
- Leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

### 25. Fault Tolerant Control Using Fractional-order Terminal Sliding Mode Control for Robotic Manipulators (2018) -- Saim Ahmed; Haoping Wang; Yang Tian
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- Makes less novel: General claim that actuator nonidealities matter for robot control.
- Leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

### 26. Reinforcement Learning-Based Fixed-Time Trajectory Tracking Control for Uncertain Robotic Manipulators With Input Saturation (2021) -- Shengjie Cao; Liang Sun; Jingjing Jiang; Zongyu Zuo
- Problem claimed: Control manipulators while respecting torque, velocity, or input constraints.
- Mechanism introduced: Constrained optimization, model predictive control, anti-windup, or control allocation.
- Hidden assumptions: Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate.
- Variables fixed: Actuator coordinates, contact primitive set, and sign-specific effort margins.
- Failure modes ignored: Directional limits that make one branch/contact primitive safer than another for the same object motion.
- Makes less novel: Novelty of merely adding actuator limits to a controller.
- Leaves open: A policy representation where signed actuation cones choose the manipulation primitive itself.

### 27. Fuzzy Adaptive Consensus Control for Nonlinear Multiagent Systems With Intermittent Actuator Faults (2021) -- Wei Wu; Shaocheng Tong
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- Makes less novel: General claim that actuator nonidealities matter for robot control.
- Leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

### 28. Fault tolerant control for robotic manipulator using fractional-order backstepping fast terminal sliding mode control (2021) -- Zeeshan Anjum; Yu Guo; Wei Yao
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- Makes less novel: General claim that actuator nonidealities matter for robot control.
- Leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

### 29. Fault Tolerant Control Scheme for Robotic Manipulators Affected by Torque Faults (2018) -- Alessandro Freddi; Sauro Longhi; Andrea Monteriù; D. Ortenzi; D. Proietti Pagnotta
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- Makes less novel: General claim that actuator nonidealities matter for robot control.
- Leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

### 30. Disturbance‐observer‐based fault‐tolerant control of robotic manipulator: A fixed‐time adaptive approach (2024) -- Zeeshan Anjum; Zhe Sun; Bo Chen
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- Makes less novel: General claim that actuator nonidealities matter for robot control.
- Leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

### 31. Adaptive fixed-time fuzzy fault-tolerant control for robotic manipulator with unknown friction and composite actuator faults (2024) -- Yuqiang Zhu; Zhen Liu; Baoping Jiang; Quanmin Zhu
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- Makes less novel: General claim that actuator nonidealities matter for robot control.
- Leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

### 32. Stiff and safe task-space position and attitude controller for robotic manipulators (2020) -- Gyuho Byun; Ryo Kikuuwe
- Problem claimed: Control manipulators while respecting torque, velocity, or input constraints.
- Mechanism introduced: Constrained optimization, model predictive control, anti-windup, or control allocation.
- Hidden assumptions: Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate.
- Variables fixed: Actuator coordinates, contact primitive set, and sign-specific effort margins.
- Failure modes ignored: Directional limits that make one branch/contact primitive safer than another for the same object motion.
- Makes less novel: Novelty of merely adding actuator limits to a controller.
- Leaves open: A policy representation where signed actuation cones choose the manipulation primitive itself.

### 33. Towards Developing Gripper to obtain Dexterous Manipulation (2018) -- Nahian Rahman
- Problem claimed: Control manipulators while respecting torque, velocity, or input constraints.
- Mechanism introduced: Constrained optimization, model predictive control, anti-windup, or control allocation.
- Hidden assumptions: Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate.
- Variables fixed: Actuator coordinates, contact primitive set, and sign-specific effort margins.
- Failure modes ignored: Directional limits that make one branch/contact primitive safer than another for the same object motion.
- Makes less novel: Novelty of merely adding actuator limits to a controller.
- Leaves open: A policy representation where signed actuation cones choose the manipulation primitive itself.

### 34. Adaptive nonsingular fixed-time sliding mode control for uncertain robotic manipulators under actuator saturation (2021) -- Huayang Sai; Zhenbang Xu; Shuai He; Enyang Zhang; Lin Zhu
- Problem claimed: Control manipulators while respecting torque, velocity, or input constraints.
- Mechanism introduced: Constrained optimization, model predictive control, anti-windup, or control allocation.
- Hidden assumptions: Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate.
- Variables fixed: Actuator coordinates, contact primitive set, and sign-specific effort margins.
- Failure modes ignored: Directional limits that make one branch/contact primitive safer than another for the same object motion.
- Makes less novel: Novelty of merely adding actuator limits to a controller.
- Leaves open: A policy representation where signed actuation cones choose the manipulation primitive itself.

### 35. Integrated State/Fault Estimation and Fault-Tolerant Control Design for Switched T–S Fuzzy Systems With Sensor and Actuator Faults (2021) -- Ayyoub Ait Ladel; Abdellah Benzaouia; Rachid Outbib; Mustapha Ouladsine
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- Makes less novel: General claim that actuator nonidealities matter for robot control.
- Leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

### 36. WALK‐MAN: A High‐Performance Humanoid Platform for Realistic Environments (2017) -- Nikos G. Tsagarakis; Darwin G. Caldwell; Francesca Negrello; Wooseok Choi; Lorenzo Baccelliere; Vo-Gia Loc; et al.
- Problem claimed: Improve robot control, planning, or modeling under physical uncertainty.
- Mechanism introduced: Model-based control, planning, estimation, or learning depending on the paper.
- Hidden assumptions: Actuator authority is either nominal, symmetric, or hidden inside an uncertainty set.
- Variables fixed: Task action basis, actuator sign geometry, and controller-policy boundary.
- Failure modes ignored: Direction-specific action feasibility and its effect on manipulation primitive choice.
- Makes less novel: Broad claim that robustness is important.
- Leaves open: Explicit actuator-asymmetry structure inside the manipulation policy.

### 37. Dynamic learning-based fault tolerant control for robotic manipulators with actuator faults (2022) -- Fukai Zhang; Weiming Wu; Rui Song; Cong Wang
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- Makes less novel: General claim that actuator nonidealities matter for robot control.
- Leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

### 38. On the design of fault-tolerant robotic manipulator systems (1993) -- Delbert Tesar
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- Makes less novel: General claim that actuator nonidealities matter for robot control.
- Leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

### 39. Adaptive decentralized finite‐time output tracking control for MIMO interconnected nonlinear systems with output constraints and actuator faults (2017) -- Xu Jin
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- Makes less novel: General claim that actuator nonidealities matter for robot control.
- Leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

### 40. A novel robust fixed‐time fault‐tolerant tracking control of uncertain robot manipulators (2020) -- Linzhi Liu; Liyin Zhang; Youming Wang; Yinlong Hou
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- Makes less novel: General claim that actuator nonidealities matter for robot control.
- Leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

### 41. Robust fault tolerant control based on adaptive observer for Takagi-Sugeno fuzzy systems with sensor and actuator faults: Application to single-link manipulator (2020) -- Salama Makni; Maha Bouattour; Ahmed El Hajjaji; Mohamed Chaabane
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- Makes less novel: General claim that actuator nonidealities matter for robot control.
- Leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

### 42. Synergy-based interface for bilateral tele-manipulations of a master-slave system with large asymmetries (2016) -- Anais Brygo; Ioannis Sarakoglou; Arash Ajoudani; Nadia Garcia-Hernández; Giorgio Grioli; Manuel G. Catalano; et al.
- Problem claimed: Make contact-rich manipulation stable and compliant under uncertain contacts.
- Mechanism introduced: Impedance/admittance control, force feedback, or variable compliance.
- Hidden assumptions: The commanded wrench/velocity is realizable symmetrically enough by the actuators.
- Variables fixed: Directional actuator authority and mode-dependent actuation costs.
- Failure modes ignored: Contact strategies that become unstable because one corrective direction is weaker than its opposite.
- Makes less novel: Novelty of using compliant feedback for manipulation.
- Leaves open: A signed feasibility layer that tells compliance policies which corrections are physically cheap.

### 43. A compact drive system for geared robotic joints and actuation mechanisms (2016) -- Elias Brassitos
- Problem claimed: Improve robot control, planning, or modeling under physical uncertainty.
- Mechanism introduced: Model-based control, planning, estimation, or learning depending on the paper.
- Hidden assumptions: Actuator authority is either nominal, symmetric, or hidden inside an uncertainty set.
- Variables fixed: Task action basis, actuator sign geometry, and controller-policy boundary.
- Failure modes ignored: Direction-specific action feasibility and its effect on manipulation primitive choice.
- Makes less novel: Broad claim that robustness is important.
- Leaves open: Explicit actuator-asymmetry structure inside the manipulation policy.

### 44. Grasp Stability Analysis with Passive Reactions (2021) -- Maximilian Haas-Heger
- Problem claimed: Control manipulators while respecting torque, velocity, or input constraints.
- Mechanism introduced: Constrained optimization, model predictive control, anti-windup, or control allocation.
- Hidden assumptions: Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate.
- Variables fixed: Actuator coordinates, contact primitive set, and sign-specific effort margins.
- Failure modes ignored: Directional limits that make one branch/contact primitive safer than another for the same object motion.
- Makes less novel: Novelty of merely adding actuator limits to a controller.
- Leaves open: A policy representation where signed actuation cones choose the manipulation primitive itself.

### 45. Reconfigurable Tolerant Control of Uncertain Mechanical Systems With Actuator Faults: A Sliding Mode Observer-Based Approach (2017) -- Bing Xiao; Shen Yin; Huijun Gao
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- Makes less novel: General claim that actuator nonidealities matter for robot control.
- Leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.
