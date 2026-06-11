# Hostile Prior Work Set

This set contains the 100 papers most likely to narrow or attack the contribution because they already address robot robustness, actuator faults/constraints, contact manipulation, dynamics mismatch, or action-model choices.

## 1. Adaptive PID-like fault-tolerant control for robot manipulators with given performance specifications (2018) -- Ye Cao; Yongduan Song
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 2. Dual arm coordination of redundant space manipulators mounted on a spacecraft (2023) -- S. Kalaycioglu; Anton de Ruiter
- Problem claimed: Control manipulators while respecting torque, velocity, or input constraints.
- Actual mechanism introduced: Constrained optimization, model predictive control, anti-windup, or control allocation.
- Hidden assumptions: Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate.
- Variables treated as fixed: Actuator coordinates, contact primitive set, and sign-specific effort margins.
- Failure modes ignored: Directional limits that make one branch/contact primitive safer than another for the same object motion.
- What it makes less novel: Novelty of merely adding actuator limits to a controller.
- What it leaves open: A policy representation where signed actuation cones choose the manipulation primitive itself.

## 3. Neural Networks-Based Fault Tolerant Control of a Robot via Fast Terminal Sliding Mode (2019) -- Shuang Zhang; Pengxin Yang; Linghuan Kong; Wenshi Chen; Qiang Fu; Kaixiang Peng
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 4. The Control Handbook (2005) -- William S. Levine
- Problem claimed: Control manipulators while respecting torque, velocity, or input constraints.
- Actual mechanism introduced: Constrained optimization, model predictive control, anti-windup, or control allocation.
- Hidden assumptions: Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate.
- Variables treated as fixed: Actuator coordinates, contact primitive set, and sign-specific effort margins.
- Failure modes ignored: Directional limits that make one branch/contact primitive safer than another for the same object motion.
- What it makes less novel: Novelty of merely adding actuator limits to a controller.
- What it leaves open: A policy representation where signed actuation cones choose the manipulation primitive itself.

## 5. Finite-Time Adaptive Fault-Tolerant Control for Robot Manipulators With Guaranteed Transient Performance (2025) -- Yongling Xia; Yeqing Yuan; Weichao Sun
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 6. Adaptive fault tolerant control for a class of input and state constrained MIMO nonlinear systems (2015) -- Xu Jin
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 7. Control of robot manipulators with consideration of actuator performance degradation and failures (2002) -- Guangjun Liu
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 8. Highly‐Aligned All‐Fiber Actuator with Asymmetric Photothermal‐Humidity Response and Autonomous Perceptivity (2024) -- Yufan Zhang; Xinran Zhou; Luyun Liu; Shuang Wang; Yue Zhang; Mengjie Wu; et al.
- Problem claimed: Improve robot control, planning, or modeling under physical uncertainty.
- Actual mechanism introduced: Model-based control, planning, estimation, or learning depending on the paper.
- Hidden assumptions: Actuator authority is either nominal, symmetric, or hidden inside an uncertainty set.
- Variables treated as fixed: Task action basis, actuator sign geometry, and controller-policy boundary.
- Failure modes ignored: Direction-specific action feasibility and its effect on manipulation primitive choice.
- What it makes less novel: Broad claim that robustness is important.
- What it leaves open: Explicit actuator-asymmetry structure inside the manipulation policy.

## 9. Advanced Control Strategies for Space Systems: Integration of Model Predictive Control and Neural Networks (2025) -- Sean Kalaycioglu; Anton de Ruiter
- Problem claimed: Control manipulators while respecting torque, velocity, or input constraints.
- Actual mechanism introduced: Constrained optimization, model predictive control, anti-windup, or control allocation.
- Hidden assumptions: Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate.
- Variables treated as fixed: Actuator coordinates, contact primitive set, and sign-specific effort margins.
- Failure modes ignored: Directional limits that make one branch/contact primitive safer than another for the same object motion.
- What it makes less novel: Novelty of merely adding actuator limits to a controller.
- What it leaves open: A policy representation where signed actuation cones choose the manipulation primitive itself.

## 10. Finite‐time fault‐tolerant adaptive robust control for a class of uncertain non‐linear systems with saturation constraints using integral backstepping approach (2018) -- Seyed Majid Smaeilzadeh; Mehdi Golestani
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 11. Fuzzy Disturbance Observers-Based Adaptive Fault-Tolerant Control for an Uncertain Constrained Automatic Flexible Robotic Manipulator (2023) -- Yong Ren; Yaobin Sun; Lei Liu
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 12. Fault-tolerant scheme for robotic manipulator—Nonlinear robust back-stepping control with friction compensation (2021) -- Khurram Ali; Adeel Mehmood; Jamshed Iqbal
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 13. Robust Adaptive Fuzzy Fault Tolerant Control of Robot Manipulators With Unknown Parameters (2023) -- Shoulin Xu; Bin He
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 14. Fixed-Time Fuzzy Resilient Consensus Tracking of Nonlinear MASs Under DoS Attacks and Actuator Faults (2024) -- Bo Xu; Yuan‐Xin Li; Zhongsheng Hou
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 15. First-Principles Models and Safety-Driven Planning for Soft and Rigid Robots (2025) -- Zachary Brei
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 16. Disturbance Observer-Based Fault-Tolerant Control for Robotic Systems With Guaranteed Prescribed Performance (2020) -- Haifeng Huang; Wei He; Jiashu Li; Bin Xu; Chenguang Yang; Weicun Zhang
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 17. Fault-tolerant control strategies for industrial robots: state of the art and future perspective on AI-based fault management (2025) -- Zeashan Hameed Khan; Ali A. Nasir; Samir Mekid
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 18. Push, Press, Slide: Mode-Aware Planar Contact Manipulation via Reduced-Order Models (2026) -- Melih Özcan; Orguner, Umut; Oguz, Ozgur S.
- Problem claimed: Plan and control object motion through intermittent or sticking contact.
- Actual mechanism introduced: Quasi-static pushing models, motion cones, contact-mode planning, or learned push dynamics.
- Hidden assumptions: The robot can realize planned pusher motions equally well in each direction.
- Variables treated as fixed: The robot-side actuator cone behind the contact-mode model.
- Failure modes ignored: A push mode may be geometrically valid but actuator-directionally brittle.
- What it makes less novel: Novelty of contact-mode or pushing mechanics alone.
- What it leaves open: Jointly selecting contact/IK primitive and signed actuator cone feasibility.

## 19. Indirect Adaptive Robust Control of Hydraulic Manipulators With Accurate Parameter Estimates (2010) -- Amit Mohanty; Bin Yao
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 20. Adaptive Fault Tolerant Non-Singular Sliding Mode Control for Robotic Manipulators Based on Fixed-Time Control Law (2022) -- Saim Ahmed; Ahmad Taher Azar; Mohamed Tounsi
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 21. A Dynamic Programming Framework for Optimal Planning of Redundant Robots Along Prescribed Paths With Kineto-Dynamic Constraints (2023) -- Enrico Ferrentino; Heitor J. Savino; Antonio Franchi; Pasquale Chiacchio
- Problem claimed: Control manipulators while respecting torque, velocity, or input constraints.
- Actual mechanism introduced: Constrained optimization, model predictive control, anti-windup, or control allocation.
- Hidden assumptions: Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate.
- Variables treated as fixed: Actuator coordinates, contact primitive set, and sign-specific effort margins.
- Failure modes ignored: Directional limits that make one branch/contact primitive safer than another for the same object motion.
- What it makes less novel: Novelty of merely adding actuator limits to a controller.
- What it leaves open: A policy representation where signed actuation cones choose the manipulation primitive itself.

## 22. Coupling Magnetic Torque and Force for Colloidal Microbot Assembly and Manipulation (2023) -- Coy J. Zimmermann; Andrew J. Petruska; Keith B. Neeves; David W. M. Marr
- Problem claimed: Improve robot control, planning, or modeling under physical uncertainty.
- Actual mechanism introduced: Model-based control, planning, estimation, or learning depending on the paper.
- Hidden assumptions: Actuator authority is either nominal, symmetric, or hidden inside an uncertainty set.
- Variables treated as fixed: Task action basis, actuator sign geometry, and controller-policy boundary.
- Failure modes ignored: Direction-specific action feasibility and its effect on manipulation primitive choice.
- What it makes less novel: Broad claim that robustness is important.
- What it leaves open: Explicit actuator-asymmetry structure inside the manipulation policy.

## 23. Fault detection and robust fault recovery control for robot manipulators with actuator failures (2003) -- Jin-Ho Shin; Ju-Jang Lee
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 24. Active Fault-Tolerant Control Design for Actuator Fault Mitigation in Robotic Manipulators (2021) -- Yashar Shabbouei Hagh; Reza Mohammadi Asl; Afef Fekih; Huapeng Wu; Heikki Handroos
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 25. Fault Tolerant Control Using Fractional-order Terminal Sliding Mode Control for Robotic Manipulators (2018) -- Saim Ahmed; Haoping Wang; Yang Tian
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 26. Reinforcement Learning-Based Fixed-Time Trajectory Tracking Control for Uncertain Robotic Manipulators With Input Saturation (2021) -- Shengjie Cao; Liang Sun; Jingjing Jiang; Zongyu Zuo
- Problem claimed: Control manipulators while respecting torque, velocity, or input constraints.
- Actual mechanism introduced: Constrained optimization, model predictive control, anti-windup, or control allocation.
- Hidden assumptions: Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate.
- Variables treated as fixed: Actuator coordinates, contact primitive set, and sign-specific effort margins.
- Failure modes ignored: Directional limits that make one branch/contact primitive safer than another for the same object motion.
- What it makes less novel: Novelty of merely adding actuator limits to a controller.
- What it leaves open: A policy representation where signed actuation cones choose the manipulation primitive itself.

## 27. Fuzzy Adaptive Consensus Control for Nonlinear Multiagent Systems With Intermittent Actuator Faults (2021) -- Wei Wu; Shaocheng Tong
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 28. Fault tolerant control for robotic manipulator using fractional-order backstepping fast terminal sliding mode control (2021) -- Zeeshan Anjum; Yu Guo; Wei Yao
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 29. Fault Tolerant Control Scheme for Robotic Manipulators Affected by Torque Faults (2018) -- Alessandro Freddi; Sauro Longhi; Andrea Monteriù; D. Ortenzi; D. Proietti Pagnotta
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 30. Disturbance‐observer‐based fault‐tolerant control of robotic manipulator: A fixed‐time adaptive approach (2024) -- Zeeshan Anjum; Zhe Sun; Bo Chen
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 31. Adaptive fixed-time fuzzy fault-tolerant control for robotic manipulator with unknown friction and composite actuator faults (2024) -- Yuqiang Zhu; Zhen Liu; Baoping Jiang; Quanmin Zhu
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 32. Stiff and safe task-space position and attitude controller for robotic manipulators (2020) -- Gyuho Byun; Ryo Kikuuwe
- Problem claimed: Control manipulators while respecting torque, velocity, or input constraints.
- Actual mechanism introduced: Constrained optimization, model predictive control, anti-windup, or control allocation.
- Hidden assumptions: Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate.
- Variables treated as fixed: Actuator coordinates, contact primitive set, and sign-specific effort margins.
- Failure modes ignored: Directional limits that make one branch/contact primitive safer than another for the same object motion.
- What it makes less novel: Novelty of merely adding actuator limits to a controller.
- What it leaves open: A policy representation where signed actuation cones choose the manipulation primitive itself.

## 33. Towards Developing Gripper to obtain Dexterous Manipulation (2018) -- Nahian Rahman
- Problem claimed: Control manipulators while respecting torque, velocity, or input constraints.
- Actual mechanism introduced: Constrained optimization, model predictive control, anti-windup, or control allocation.
- Hidden assumptions: Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate.
- Variables treated as fixed: Actuator coordinates, contact primitive set, and sign-specific effort margins.
- Failure modes ignored: Directional limits that make one branch/contact primitive safer than another for the same object motion.
- What it makes less novel: Novelty of merely adding actuator limits to a controller.
- What it leaves open: A policy representation where signed actuation cones choose the manipulation primitive itself.

## 34. Adaptive nonsingular fixed-time sliding mode control for uncertain robotic manipulators under actuator saturation (2021) -- Huayang Sai; Zhenbang Xu; Shuai He; Enyang Zhang; Lin Zhu
- Problem claimed: Control manipulators while respecting torque, velocity, or input constraints.
- Actual mechanism introduced: Constrained optimization, model predictive control, anti-windup, or control allocation.
- Hidden assumptions: Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate.
- Variables treated as fixed: Actuator coordinates, contact primitive set, and sign-specific effort margins.
- Failure modes ignored: Directional limits that make one branch/contact primitive safer than another for the same object motion.
- What it makes less novel: Novelty of merely adding actuator limits to a controller.
- What it leaves open: A policy representation where signed actuation cones choose the manipulation primitive itself.

## 35. Integrated State/Fault Estimation and Fault-Tolerant Control Design for Switched T–S Fuzzy Systems With Sensor and Actuator Faults (2021) -- Ayyoub Ait Ladel; Abdellah Benzaouia; Rachid Outbib; Mustapha Ouladsine
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 36. WALK‐MAN: A High‐Performance Humanoid Platform for Realistic Environments (2017) -- Nikos G. Tsagarakis; Darwin G. Caldwell; Francesca Negrello; Wooseok Choi; Lorenzo Baccelliere; Vo-Gia Loc; et al.
- Problem claimed: Improve robot control, planning, or modeling under physical uncertainty.
- Actual mechanism introduced: Model-based control, planning, estimation, or learning depending on the paper.
- Hidden assumptions: Actuator authority is either nominal, symmetric, or hidden inside an uncertainty set.
- Variables treated as fixed: Task action basis, actuator sign geometry, and controller-policy boundary.
- Failure modes ignored: Direction-specific action feasibility and its effect on manipulation primitive choice.
- What it makes less novel: Broad claim that robustness is important.
- What it leaves open: Explicit actuator-asymmetry structure inside the manipulation policy.

## 37. Dynamic learning-based fault tolerant control for robotic manipulators with actuator faults (2022) -- Fukai Zhang; Weiming Wu; Rui Song; Cong Wang
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 38. On the design of fault-tolerant robotic manipulator systems (1993) -- Delbert Tesar
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 39. Adaptive decentralized finite‐time output tracking control for MIMO interconnected nonlinear systems with output constraints and actuator faults (2017) -- Xu Jin
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 40. A novel robust fixed‐time fault‐tolerant tracking control of uncertain robot manipulators (2020) -- Linzhi Liu; Liyin Zhang; Youming Wang; Yinlong Hou
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 41. Robust fault tolerant control based on adaptive observer for Takagi-Sugeno fuzzy systems with sensor and actuator faults: Application to single-link manipulator (2020) -- Salama Makni; Maha Bouattour; Ahmed El Hajjaji; Mohamed Chaabane
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 42. Synergy-based interface for bilateral tele-manipulations of a master-slave system with large asymmetries (2016) -- Anais Brygo; Ioannis Sarakoglou; Arash Ajoudani; Nadia Garcia-Hernández; Giorgio Grioli; Manuel G. Catalano; et al.
- Problem claimed: Make contact-rich manipulation stable and compliant under uncertain contacts.
- Actual mechanism introduced: Impedance/admittance control, force feedback, or variable compliance.
- Hidden assumptions: The commanded wrench/velocity is realizable symmetrically enough by the actuators.
- Variables treated as fixed: Directional actuator authority and mode-dependent actuation costs.
- Failure modes ignored: Contact strategies that become unstable because one corrective direction is weaker than its opposite.
- What it makes less novel: Novelty of using compliant feedback for manipulation.
- What it leaves open: A signed feasibility layer that tells compliance policies which corrections are physically cheap.

## 43. A compact drive system for geared robotic joints and actuation mechanisms (2016) -- Elias Brassitos
- Problem claimed: Improve robot control, planning, or modeling under physical uncertainty.
- Actual mechanism introduced: Model-based control, planning, estimation, or learning depending on the paper.
- Hidden assumptions: Actuator authority is either nominal, symmetric, or hidden inside an uncertainty set.
- Variables treated as fixed: Task action basis, actuator sign geometry, and controller-policy boundary.
- Failure modes ignored: Direction-specific action feasibility and its effect on manipulation primitive choice.
- What it makes less novel: Broad claim that robustness is important.
- What it leaves open: Explicit actuator-asymmetry structure inside the manipulation policy.

## 44. Grasp Stability Analysis with Passive Reactions (2021) -- Maximilian Haas-Heger
- Problem claimed: Control manipulators while respecting torque, velocity, or input constraints.
- Actual mechanism introduced: Constrained optimization, model predictive control, anti-windup, or control allocation.
- Hidden assumptions: Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate.
- Variables treated as fixed: Actuator coordinates, contact primitive set, and sign-specific effort margins.
- Failure modes ignored: Directional limits that make one branch/contact primitive safer than another for the same object motion.
- What it makes less novel: Novelty of merely adding actuator limits to a controller.
- What it leaves open: A policy representation where signed actuation cones choose the manipulation primitive itself.

## 45. Reconfigurable Tolerant Control of Uncertain Mechanical Systems With Actuator Faults: A Sliding Mode Observer-Based Approach (2017) -- Bing Xiao; Shen Yin; Huijun Gao
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 46. Ferrofluids and bio-ferrofluids: looking back and stepping forward (2022) -- V. Socoliuc; М. В. Авдеев; V. Kuncser; Rodica Turcu; Etelka Tombácz; L. Vékás
- Problem claimed: Improve robot control, planning, or modeling under physical uncertainty.
- Actual mechanism introduced: Model-based control, planning, estimation, or learning depending on the paper.
- Hidden assumptions: Actuator authority is either nominal, symmetric, or hidden inside an uncertainty set.
- Variables treated as fixed: Task action basis, actuator sign geometry, and controller-policy boundary.
- Failure modes ignored: Direction-specific action feasibility and its effect on manipulation primitive choice.
- What it makes less novel: Broad claim that robustness is important.
- What it leaves open: Explicit actuator-asymmetry structure inside the manipulation policy.

## 47. Multifunctional Magnetic Muscles for Soft Robotics (2024) -- Minho Seong; Kahyun Sun; Somi Kim; Hyukjoo Kwon; Sang-Woo Lee; Sarath Chandra Veerla; et al.
- Problem claimed: Improve robot control, planning, or modeling under physical uncertainty.
- Actual mechanism introduced: Model-based control, planning, estimation, or learning depending on the paper.
- Hidden assumptions: Actuator authority is either nominal, symmetric, or hidden inside an uncertainty set.
- Variables treated as fixed: Task action basis, actuator sign geometry, and controller-policy boundary.
- Failure modes ignored: Direction-specific action feasibility and its effect on manipulation primitive choice.
- What it makes less novel: Broad claim that robustness is important.
- What it leaves open: Explicit actuator-asymmetry structure inside the manipulation policy.

## 48. Finite Time Fault Tolerant Control for Robot Manipulators Using Time Delay Estimation and Continuous Nonsingular Fast Terminal Sliding Mode Control (2016) -- Mien Van; Shuzhi Sam Ge; Hongliang Ren
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 49. Nature-inspired miniaturized magnetic soft robotic swimmers (2024) -- R. Pramanik; Roel Verstappen; Patrick R. Onck
- Problem claimed: Improve robot control, planning, or modeling under physical uncertainty.
- Actual mechanism introduced: Model-based control, planning, estimation, or learning depending on the paper.
- Hidden assumptions: Actuator authority is either nominal, symmetric, or hidden inside an uncertainty set.
- Variables treated as fixed: Task action basis, actuator sign geometry, and controller-policy boundary.
- Failure modes ignored: Direction-specific action feasibility and its effect on manipulation primitive choice.
- What it makes less novel: Broad claim that robustness is important.
- What it leaves open: Explicit actuator-asymmetry structure inside the manipulation policy.

## 50. Dig-Grasping via Direct Quasistatic Interaction Using Asymmetric Fingers: An Approach to Effective Bin Picking (2021) -- Zhekai Tong; Yu Hin Ng; Chung Hee Kim; Tierui He; Jungwon Seo
- Problem claimed: Plan and control object motion through intermittent or sticking contact.
- Actual mechanism introduced: Quasi-static pushing models, motion cones, contact-mode planning, or learned push dynamics.
- Hidden assumptions: The robot can realize planned pusher motions equally well in each direction.
- Variables treated as fixed: The robot-side actuator cone behind the contact-mode model.
- Failure modes ignored: A push mode may be geometrically valid but actuator-directionally brittle.
- What it makes less novel: Novelty of contact-mode or pushing mechanics alone.
- What it leaves open: Jointly selecting contact/IK primitive and signed actuator cone feasibility.

## 51. Cartesian Control for Robot Manipulators (2010) -- Pablo Sánchez‐Sánchez; Fernando Reyes
- Problem claimed: Control manipulators while respecting torque, velocity, or input constraints.
- Actual mechanism introduced: Constrained optimization, model predictive control, anti-windup, or control allocation.
- Hidden assumptions: Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate.
- Variables treated as fixed: Actuator coordinates, contact primitive set, and sign-specific effort margins.
- Failure modes ignored: Directional limits that make one branch/contact primitive safer than another for the same object motion.
- What it makes less novel: Novelty of merely adding actuator limits to a controller.
- What it leaves open: A policy representation where signed actuation cones choose the manipulation primitive itself.

## 52. Synergy-Based Bilateral Port: A Universal Control Module for Tele-Manipulation Frameworks Using Asymmetric Master–Slave Systems (2017) -- Anais Brygo; Ioannis Sarakoglou; Giorgio Grioli; Nikos G. Tsagarakis
- Problem claimed: Make contact-rich manipulation stable and compliant under uncertain contacts.
- Actual mechanism introduced: Impedance/admittance control, force feedback, or variable compliance.
- Hidden assumptions: The commanded wrench/velocity is realizable symmetrically enough by the actuators.
- Variables treated as fixed: Directional actuator authority and mode-dependent actuation costs.
- Failure modes ignored: Contact strategies that become unstable because one corrective direction is weaker than its opposite.
- What it makes less novel: Novelty of using compliant feedback for manipulation.
- What it leaves open: A signed feasibility layer that tells compliance policies which corrections are physically cheap.

## 53. Toward Dexterous Manipulation With Augmented Adaptive Synergies: The Pisa/IIT SoftHand 2 (2018) -- Cosimo Della Santina; Cristina Piazza; Giorgio Grioli; Manuel G. Catalano; Antonio Bicchi
- Problem claimed: Improve robot control, planning, or modeling under physical uncertainty.
- Actual mechanism introduced: Model-based control, planning, estimation, or learning depending on the paper.
- Hidden assumptions: Actuator authority is either nominal, symmetric, or hidden inside an uncertainty set.
- Variables treated as fixed: Task action basis, actuator sign geometry, and controller-policy boundary.
- Failure modes ignored: Direction-specific action feasibility and its effect on manipulation primitive choice.
- What it makes less novel: Broad claim that robustness is important.
- What it leaves open: Explicit actuator-asymmetry structure inside the manipulation policy.

## 54. Intelligent Impedance Strategy for Force–Motion Control of Robotic Manipulators in Unknown Environments via Expert-Guided Deep Reinforcement Learning (2025) -- Hui Shao; Weishi Hu; Li Yang; Wei Wang; Satoshi Suzuki; Zhiwei Gao
- Problem claimed: Make contact-rich manipulation stable and compliant under uncertain contacts.
- Actual mechanism introduced: Impedance/admittance control, force feedback, or variable compliance.
- Hidden assumptions: The commanded wrench/velocity is realizable symmetrically enough by the actuators.
- Variables treated as fixed: Directional actuator authority and mode-dependent actuation costs.
- Failure modes ignored: Contact strategies that become unstable because one corrective direction is weaker than its opposite.
- What it makes less novel: Novelty of using compliant feedback for manipulation.
- What it leaves open: A signed feasibility layer that tells compliance policies which corrections are physically cheap.

## 55. Adaptive Fixed-Time Fault-Tolerant Tracking Control and Its Application for Robot Manipulators (2021) -- Liyin Zhang; Hui Liu; Dafeng Tang; Yinlong Hou; Youming Wang
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 56. A Graphene‐Mica‐Based Photo‐Thermal Actuator for Small‐Scale Soft Robots (2024) -- Ming Gu; T. J. Echtermeyer
- Problem claimed: Improve robot control, planning, or modeling under physical uncertainty.
- Actual mechanism introduced: Model-based control, planning, estimation, or learning depending on the paper.
- Hidden assumptions: Actuator authority is either nominal, symmetric, or hidden inside an uncertainty set.
- Variables treated as fixed: Task action basis, actuator sign geometry, and controller-policy boundary.
- Failure modes ignored: Direction-specific action feasibility and its effect on manipulation primitive choice.
- What it makes less novel: Broad claim that robustness is important.
- What it leaves open: Explicit actuator-asymmetry structure inside the manipulation policy.

## 57. A Robust Hybrid Position/Force Control Considering Motor Torque Saturation (2021) -- Takashi Ohhira; Keinosuke Yokota; Shuichi Tatsumi; Toshiyuki Murakami
- Problem claimed: Control manipulators while respecting torque, velocity, or input constraints.
- Actual mechanism introduced: Constrained optimization, model predictive control, anti-windup, or control allocation.
- Hidden assumptions: Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate.
- Variables treated as fixed: Actuator coordinates, contact primitive set, and sign-specific effort margins.
- Failure modes ignored: Directional limits that make one branch/contact primitive safer than another for the same object motion.
- What it makes less novel: Novelty of merely adding actuator limits to a controller.
- What it leaves open: A policy representation where signed actuation cones choose the manipulation primitive itself.

## 58. Exploring How Non-Prehensile Manipulation Expands Capability in Robots Experiencing Multi-Joint Failure (2024) -- Gilberto Briscoe-Martinez; Anuj Pasricha; Ava Abderezaei; Santosh Chaganti; Sarath Chandra Vajrala; Sri Kanth Popuri; et al.
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 59. Nonlinear Model Predictive Control with Enhanced Actuator Model for Multi-Rotor Aerial Vehicles with Generic Designs (2020) -- Davide Bicego; Jacopo Mazzetto; Ruggero Carli; Marcello Farina; Antonio Franchi
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 60. A multifunctional soft robotic shape display with high-speed actuation, sensing, and control (2023) -- Brian K. Johnson; Mantas Naris; Vani Sundaram; Angella Volchko; Kevin Ly; Shane K. Mitchell; et al.
- Problem claimed: Improve robot control, planning, or modeling under physical uncertainty.
- Actual mechanism introduced: Model-based control, planning, estimation, or learning depending on the paper.
- Hidden assumptions: Actuator authority is either nominal, symmetric, or hidden inside an uncertainty set.
- Variables treated as fixed: Task action basis, actuator sign geometry, and controller-policy boundary.
- Failure modes ignored: Direction-specific action feasibility and its effect on manipulation primitive choice.
- What it makes less novel: Broad claim that robustness is important.
- What it leaves open: Explicit actuator-asymmetry structure inside the manipulation policy.

## 61. Fully Adaptive-Gain-Based Intelligent Failure-Tolerant Control for Spacecraft Attitude Stabilization Under Actuator Saturation (2020) -- Ning Zhou; Xiaodong Cheng; Yuanqing Xia; Yan‐Jun Liu
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 62. Fault Diagnosis and Fault-Tolerant Control of Uncertain Robot Manipulators Using High-Order Sliding Mode (2016) -- Mien Van; Pasquale Franciosa; Dariusz Ceglarek
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 63. Operational Space Control of Constrained and Underactuated Systems (2012) -- Michael Mistry; Ludovic Righetti
- Problem claimed: Control manipulators while respecting torque, velocity, or input constraints.
- Actual mechanism introduced: Constrained optimization, model predictive control, anti-windup, or control allocation.
- Hidden assumptions: Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate.
- Variables treated as fixed: Actuator coordinates, contact primitive set, and sign-specific effort margins.
- Failure modes ignored: Directional limits that make one branch/contact primitive safer than another for the same object motion.
- What it makes less novel: Novelty of merely adding actuator limits to a controller.
- What it leaves open: A policy representation where signed actuation cones choose the manipulation primitive itself.

## 64. Neuromechanical wave resonance in jellyfish swimming (2021) -- Alexander Hoover; Nicole Xu; Brad J. Gemmell; Sean P. Colin; John H. Costello; John O. Dabiri; et al.
- Problem claimed: Control manipulators while respecting torque, velocity, or input constraints.
- Actual mechanism introduced: Constrained optimization, model predictive control, anti-windup, or control allocation.
- Hidden assumptions: Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate.
- Variables treated as fixed: Actuator coordinates, contact primitive set, and sign-specific effort margins.
- Failure modes ignored: Directional limits that make one branch/contact primitive safer than another for the same object motion.
- What it makes less novel: Novelty of merely adding actuator limits to a controller.
- What it leaves open: A policy representation where signed actuation cones choose the manipulation primitive itself.

## 65. Fault-Tolerant Dynamic Control of a Four-Wheel Redundantly-Actuated Mobile Robot (2019) -- Xiaolong Zhang; Yuanlong Xie; Liquan Jiang; Gen Li; Jie Meng; Yu Huang
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 66. A GOA-Based Fault-Tolerant Trajectory Tracking Control for an Underwater Vehicle of Multi-Thruster System Without Actuator Saturation (2023) -- Danjie Zhu; Lei Wang; Hua Zhang; Simon X. Yang
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 67. Feedback Control of the Pusher-Slider System: A Story of Hybrid and\n Underactuated Contact Dynamics (2016) -- Francois R. Hogan; Alberto Rodríguez
- Problem claimed: Control manipulators while respecting torque, velocity, or input constraints.
- Actual mechanism introduced: Constrained optimization, model predictive control, anti-windup, or control allocation.
- Hidden assumptions: Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate.
- Variables treated as fixed: Actuator coordinates, contact primitive set, and sign-specific effort margins.
- Failure modes ignored: Directional limits that make one branch/contact primitive safer than another for the same object motion.
- What it makes less novel: Novelty of merely adding actuator limits to a controller.
- What it leaves open: A policy representation where signed actuation cones choose the manipulation primitive itself.

## 68. An LPV pole-placement approach to friction compensation as an FTC problem (2012) -- Ron J. Patton; Lejun Chen; Supat Klinkhieo
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 69. Bi-enzymatic chemo-mechanical feedback loop for continuous self-sustained actuation of conducting polymers (2023) -- Serena Arnaboldi; Gerardo Salinas; Sabrina Bichon; Sébastien Gounel; Nicolas Mano; Alexander Kuhn
- Problem claimed: Improve robot control, planning, or modeling under physical uncertainty.
- Actual mechanism introduced: Model-based control, planning, estimation, or learning depending on the paper.
- Hidden assumptions: Actuator authority is either nominal, symmetric, or hidden inside an uncertainty set.
- Variables treated as fixed: Task action basis, actuator sign geometry, and controller-policy boundary.
- Failure modes ignored: Direction-specific action feasibility and its effect on manipulation primitive choice.
- What it makes less novel: Broad claim that robustness is important.
- What it leaves open: Explicit actuator-asymmetry structure inside the manipulation policy.

## 70. Human Preferences in Using Damping to Manage Singularities During Physical Human-Robot Collaboration (2020) -- Marc G. Carmichael; Richardo Khonasty; Stefano Aldini; Dikai Liu
- Problem claimed: Improve robot control, planning, or modeling under physical uncertainty.
- Actual mechanism introduced: Model-based control, planning, estimation, or learning depending on the paper.
- Hidden assumptions: Actuator authority is either nominal, symmetric, or hidden inside an uncertainty set.
- Variables treated as fixed: Task action basis, actuator sign geometry, and controller-policy boundary.
- Failure modes ignored: Direction-specific action feasibility and its effect on manipulation primitive choice.
- What it makes less novel: Broad claim that robustness is important.
- What it leaves open: Explicit actuator-asymmetry structure inside the manipulation policy.

## 71. Neural Adaptive Backstepping Control of a Robotic Manipulator With Prescribed Performance Constraint (2018) -- Qing Guo; Yi Zhang; Branko G. Celler; Steven W. Su
- Problem claimed: Control manipulators while respecting torque, velocity, or input constraints.
- Actual mechanism introduced: Constrained optimization, model predictive control, anti-windup, or control allocation.
- Hidden assumptions: Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate.
- Variables treated as fixed: Actuator coordinates, contact primitive set, and sign-specific effort margins.
- Failure modes ignored: Directional limits that make one branch/contact primitive safer than another for the same object motion.
- What it makes less novel: Novelty of merely adding actuator limits to a controller.
- What it leaves open: A policy representation where signed actuation cones choose the manipulation primitive itself.

## 72. Passive actuator fault tolerant control for a class of MIMO nonlinear systems with uncertainties (2017) -- Alireza Nasiri; Sing Kiong Nguang; Akshya Swain; Dhafer Almakhles
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 73. Fuzzy-Based Fault-Tolerant Control for Omnidirectional Mobile Robot (2020) -- Ahmad Alshorman; Omar AlShorman; Muhammad Irfan; Adam Głowacz; Fazal Muhammad; Wahyu Caesarendra
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 74. Experimental Evaluation of Aerial Manipulation Robot in Contact With 15 kV Power Line: Shielded and Long Reach Configurations (2021) -- Alejandro Suárez; Rafael Salmoral; Pedro J. Zarco-Periñán; Anı́bal Ollero
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 75. Robot Assisted Physiotherapy to Support Rehabilitation of Facial Paralysis (2013) -- Dushyantha Jayatilake; Takashi Isezaki; Yohei Teramoto; Kiyoshi Eguchi; Kenji Suzuki
- Problem claimed: Improve robot control, planning, or modeling under physical uncertainty.
- Actual mechanism introduced: Model-based control, planning, estimation, or learning depending on the paper.
- Hidden assumptions: Actuator authority is either nominal, symmetric, or hidden inside an uncertainty set.
- Variables treated as fixed: Task action basis, actuator sign geometry, and controller-policy boundary.
- Failure modes ignored: Direction-specific action feasibility and its effect on manipulation primitive choice.
- What it makes less novel: Broad claim that robustness is important.
- What it leaves open: Explicit actuator-asymmetry structure inside the manipulation policy.

## 76. Adaptive fault tolerant control for a class of multi‐input multi‐output nonlinear systems with both sensor and actuator faults (2017) -- Xu Jin
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 77. ANYpulator: Design and Control of a Safe Robotic Arm (2016) -- Karen Bodie; C. Dario Bellicoso; Marco Hutter
- Problem claimed: Make contact-rich manipulation stable and compliant under uncertain contacts.
- Actual mechanism introduced: Impedance/admittance control, force feedback, or variable compliance.
- Hidden assumptions: The commanded wrench/velocity is realizable symmetrically enough by the actuators.
- Variables treated as fixed: Directional actuator authority and mode-dependent actuation costs.
- Failure modes ignored: Contact strategies that become unstable because one corrective direction is weaker than its opposite.
- What it makes less novel: Novelty of using compliant feedback for manipulation.
- What it leaves open: A signed feasibility layer that tells compliance policies which corrections are physically cheap.

## 78. Rock-and-Walk Manipulation: Object Locomotion by Passive Rolling Dynamics and Periodic Active Control (2022) -- Abdullah Nazir; Pu Xu; Jungwon Seo
- Problem claimed: Plan and control object motion through intermittent or sticking contact.
- Actual mechanism introduced: Quasi-static pushing models, motion cones, contact-mode planning, or learned push dynamics.
- Hidden assumptions: The robot can realize planned pusher motions equally well in each direction.
- Variables treated as fixed: The robot-side actuator cone behind the contact-mode model.
- Failure modes ignored: A push mode may be geometrically valid but actuator-directionally brittle.
- What it makes less novel: Novelty of contact-mode or pushing mechanics alone.
- What it leaves open: Jointly selecting contact/IK primitive and signed actuator cone feasibility.

## 79. Coupling Field Simulation of Soft Capacitive Sensors Toward Soft Robot Perception (2023) -- Delin Hu; Haotian Li; Francesco Giorgio-Serchi; Yunjie Yang
- Problem claimed: Improve robot control, planning, or modeling under physical uncertainty.
- Actual mechanism introduced: Model-based control, planning, estimation, or learning depending on the paper.
- Hidden assumptions: Actuator authority is either nominal, symmetric, or hidden inside an uncertainty set.
- Variables treated as fixed: Task action basis, actuator sign geometry, and controller-policy boundary.
- Failure modes ignored: Direction-specific action feasibility and its effect on manipulation primitive choice.
- What it makes less novel: Broad claim that robustness is important.
- What it leaves open: Explicit actuator-asymmetry structure inside the manipulation policy.

## 80. Sim-to-real via latent prediction: Transferring visual non-prehensile manipulation policies (2023) -- Carlo Rizzardo; Fei Chen; Darwin G. Caldwell
- Problem claimed: Control manipulators while respecting torque, velocity, or input constraints.
- Actual mechanism introduced: Constrained optimization, model predictive control, anti-windup, or control allocation.
- Hidden assumptions: Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate.
- Variables treated as fixed: Actuator coordinates, contact primitive set, and sign-specific effort margins.
- Failure modes ignored: Directional limits that make one branch/contact primitive safer than another for the same object motion.
- What it makes less novel: Novelty of merely adding actuator limits to a controller.
- What it leaves open: A policy representation where signed actuation cones choose the manipulation primitive itself.

## 81. Planning of contact-interaction trajectories using numerical optimization (2020) -- Aykut Özgun Önol
- Problem claimed: Control manipulators while respecting torque, velocity, or input constraints.
- Actual mechanism introduced: Constrained optimization, model predictive control, anti-windup, or control allocation.
- Hidden assumptions: Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate.
- Variables treated as fixed: Actuator coordinates, contact primitive set, and sign-specific effort margins.
- Failure modes ignored: Directional limits that make one branch/contact primitive safer than another for the same object motion.
- What it makes less novel: Novelty of merely adding actuator limits to a controller.
- What it leaves open: A policy representation where signed actuation cones choose the manipulation primitive itself.

## 82. TacSL: A Library for Visuotactile Sensor Simulation and Learning (2024) -- Iretiayo Akinola; Jie Xu; Jan Carius; Dieter Fox; Yashraj Narang
- Problem claimed: Transfer manipulation policies across a gap between simulated and physical dynamics.
- Actual mechanism introduced: Dynamics randomization, residual adaptation, learned dynamics models, or calibration loops.
- Hidden assumptions: The policy can absorb actuator mismatch as another latent dynamics parameter; randomization support includes the relevant sign structure.
- Variables treated as fixed: The action parameterization and low-level actuator basis.
- Failure modes ignored: Structural extrapolation failure when signs share a single symmetric parameter or when weak directions demand different contact modes.
- What it makes less novel: Novelty of saying actuator mismatch hurts sim-to-real.
- What it leaves open: Whether explicit signed actuator channels outperform treating asymmetry as generic dynamics noise.

## 83. Compliant Non-Prehensile Pushing Manipulation (2025) -- Francesco Cufino; Mario Selvaggio; Fabio Amadio; Fabio Ruggiero
- Problem claimed: Make contact-rich manipulation stable and compliant under uncertain contacts.
- Actual mechanism introduced: Impedance/admittance control, force feedback, or variable compliance.
- Hidden assumptions: The commanded wrench/velocity is realizable symmetrically enough by the actuators.
- Variables treated as fixed: Directional actuator authority and mode-dependent actuation costs.
- Failure modes ignored: Contact strategies that become unstable because one corrective direction is weaker than its opposite.
- What it makes less novel: Novelty of using compliant feedback for manipulation.
- What it leaves open: A signed feasibility layer that tells compliance policies which corrections are physically cheap.

## 84. The ARMM System: An Optimized Mobile Electromagnetic Coil for Non-Linear Actuation of Flexible Surgical Instruments (2019) -- J. Sikorski; Christoff M. Heunis; Federico Franco; Sarthak Misra
- Problem claimed: Control manipulators while respecting torque, velocity, or input constraints.
- Actual mechanism introduced: Constrained optimization, model predictive control, anti-windup, or control allocation.
- Hidden assumptions: Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate.
- Variables treated as fixed: Actuator coordinates, contact primitive set, and sign-specific effort margins.
- Failure modes ignored: Directional limits that make one branch/contact primitive safer than another for the same object motion.
- What it makes less novel: Novelty of merely adding actuator limits to a controller.
- What it leaves open: A policy representation where signed actuation cones choose the manipulation primitive itself.

## 85. Light-triggered multi-joint microactuator fabricated by two-in-one femtosecond laser writing (2023) -- Xin Chen; Zhongguo Ren; Leran Zhang; Liang Yang; Dawei Wang; Yanlei Hu; et al.
- Problem claimed: Improve robot control, planning, or modeling under physical uncertainty.
- Actual mechanism introduced: Model-based control, planning, estimation, or learning depending on the paper.
- Hidden assumptions: Actuator authority is either nominal, symmetric, or hidden inside an uncertainty set.
- Variables treated as fixed: Task action basis, actuator sign geometry, and controller-policy boundary.
- Failure modes ignored: Direction-specific action feasibility and its effect on manipulation primitive choice.
- What it makes less novel: Broad claim that robustness is important.
- What it leaves open: Explicit actuator-asymmetry structure inside the manipulation policy.

## 86. Self-regulated reversal deformation and locomotion of structurally homogenous hydrogels subjected to constant light illumination (2024) -- Kexin Guo; Xuehan Yang; Chao Zhou; Chuang Li
- Problem claimed: Improve robot control, planning, or modeling under physical uncertainty.
- Actual mechanism introduced: Model-based control, planning, estimation, or learning depending on the paper.
- Hidden assumptions: Actuator authority is either nominal, symmetric, or hidden inside an uncertainty set.
- Variables treated as fixed: Task action basis, actuator sign geometry, and controller-policy boundary.
- Failure modes ignored: Direction-specific action feasibility and its effect on manipulation primitive choice.
- What it makes less novel: Broad claim that robustness is important.
- What it leaves open: Explicit actuator-asymmetry structure inside the manipulation policy.

## 87. Finite-Time Fault-Tolerant Formation Control for Distributed Multi-Vehicle Networks With Bearing Measurements (2023) -- Kefan Wu; Junyan Hu; Zhengtao Ding; Farshad Arvin
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 88. Adaptive synergies for the design and control of the Pisa/IIT SoftHand (2014) -- Manuel G. Catalano; Giorgio Grioli; Edoardo Farnioli; Alessandro Serio; Cristina Piazza; Antonio Bicchi
- Problem claimed: Improve robot control, planning, or modeling under physical uncertainty.
- Actual mechanism introduced: Model-based control, planning, estimation, or learning depending on the paper.
- Hidden assumptions: Actuator authority is either nominal, symmetric, or hidden inside an uncertainty set.
- Variables treated as fixed: Task action basis, actuator sign geometry, and controller-policy boundary.
- Failure modes ignored: Direction-specific action feasibility and its effect on manipulation primitive choice.
- What it makes less novel: Broad claim that robustness is important.
- What it leaves open: Explicit actuator-asymmetry structure inside the manipulation policy.

## 89. Linkage-Based Analysis and Optimization of an Underactuated Planar Manipulator for In-Hand Manipulation (2013) -- R. Raymond; Aaron M. Dollar
- Problem claimed: Control manipulators while respecting torque, velocity, or input constraints.
- Actual mechanism introduced: Constrained optimization, model predictive control, anti-windup, or control allocation.
- Hidden assumptions: Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate.
- Variables treated as fixed: Actuator coordinates, contact primitive set, and sign-specific effort margins.
- Failure modes ignored: Directional limits that make one branch/contact primitive safer than another for the same object motion.
- What it makes less novel: Novelty of merely adding actuator limits to a controller.
- What it leaves open: A policy representation where signed actuation cones choose the manipulation primitive itself.

## 90. Dynamic Handling Characteristics Control of an in-Wheel-Motor Driven Electric Vehicle Based on Multiple Sliding Mode Control Approach (2019) -- Minseong Chae; Young-Jin Hyun; Kyongsu Yi; Kanghyun Nam
- Problem claimed: Control manipulators while respecting torque, velocity, or input constraints.
- Actual mechanism introduced: Constrained optimization, model predictive control, anti-windup, or control allocation.
- Hidden assumptions: Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate.
- Variables treated as fixed: Actuator coordinates, contact primitive set, and sign-specific effort margins.
- Failure modes ignored: Directional limits that make one branch/contact primitive safer than another for the same object motion.
- What it makes less novel: Novelty of merely adding actuator limits to a controller.
- What it leaves open: A policy representation where signed actuation cones choose the manipulation primitive itself.

## 91. Sliding mode-based online fault compensation control for modular reconfigurable robots through adaptive dynamic programming (2021) -- Hongbing Xia; Ping Guo
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 92. Programmable inflatable origami (2023) -- Saravana Prashanth Murali Babu; Riddhi Das; Barbara Mazzolai; Ahmad Rafsanjani
- Problem claimed: Improve robot control, planning, or modeling under physical uncertainty.
- Actual mechanism introduced: Model-based control, planning, estimation, or learning depending on the paper.
- Hidden assumptions: Actuator authority is either nominal, symmetric, or hidden inside an uncertainty set.
- Variables treated as fixed: Task action basis, actuator sign geometry, and controller-policy boundary.
- Failure modes ignored: Direction-specific action feasibility and its effect on manipulation primitive choice.
- What it makes less novel: Broad claim that robustness is important.
- What it leaves open: Explicit actuator-asymmetry structure inside the manipulation policy.

## 93. Trajectory Tracking Control for Robotic Manipulator Based on Soft Actor–Critic and Generative Adversarial Imitation Learning (2024) -- Jintao Hu; Fujie Wang; Xing Li; Yi Qin; Fang Guo; Ming Jiang
- Problem claimed: Control manipulators while respecting torque, velocity, or input constraints.
- Actual mechanism introduced: Constrained optimization, model predictive control, anti-windup, or control allocation.
- Hidden assumptions: Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate.
- Variables treated as fixed: Actuator coordinates, contact primitive set, and sign-specific effort margins.
- Failure modes ignored: Directional limits that make one branch/contact primitive safer than another for the same object motion.
- What it makes less novel: Novelty of merely adding actuator limits to a controller.
- What it leaves open: A policy representation where signed actuation cones choose the manipulation primitive itself.

## 94. Safe Learning for Contact-Rich Robot Tasks: A Survey From Classical Learning-Based Methods to Safe Foundation Models (2025) -- Heng Zhang; Rui Dai; Gökhan Solak; Pokuang Zhou; Yu She; Arash Ajoudani
- Problem claimed: Control manipulators while respecting torque, velocity, or input constraints.
- Actual mechanism introduced: Constrained optimization, model predictive control, anti-windup, or control allocation.
- Hidden assumptions: Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate.
- Variables treated as fixed: Actuator coordinates, contact primitive set, and sign-specific effort margins.
- Failure modes ignored: Directional limits that make one branch/contact primitive safer than another for the same object motion.
- What it makes less novel: Novelty of merely adding actuator limits to a controller.
- What it leaves open: A policy representation where signed actuation cones choose the manipulation primitive itself.

## 95. Contact-Aware Non-prehensile Robotic Manipulation for Object Retrieval in Cluttered Environments (2023) -- Yongpeng Jiang; Yongyi Jia; Xiang Li
- Problem claimed: Control manipulators while respecting torque, velocity, or input constraints.
- Actual mechanism introduced: Constrained optimization, model predictive control, anti-windup, or control allocation.
- Hidden assumptions: Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate.
- Variables treated as fixed: Actuator coordinates, contact primitive set, and sign-specific effort margins.
- Failure modes ignored: Directional limits that make one branch/contact primitive safer than another for the same object motion.
- What it makes less novel: Novelty of merely adding actuator limits to a controller.
- What it leaves open: A policy representation where signed actuation cones choose the manipulation primitive itself.

## 96. Where to Touch, How to Contact: Hierarchical RL-MPC Framework for Geometry-Aware Long-Horizon Dexterous Manipulation (2026) -- Zhixian Xie; Yu Xiang; Michael Posa; Wanxin Jin
- Problem claimed: Transfer manipulation policies across a gap between simulated and physical dynamics.
- Actual mechanism introduced: Dynamics randomization, residual adaptation, learned dynamics models, or calibration loops.
- Hidden assumptions: The policy can absorb actuator mismatch as another latent dynamics parameter; randomization support includes the relevant sign structure.
- Variables treated as fixed: The action parameterization and low-level actuator basis.
- Failure modes ignored: Structural extrapolation failure when signs share a single symmetric parameter or when weak directions demand different contact modes.
- What it makes less novel: Novelty of saying actuator mismatch hurts sim-to-real.
- What it leaves open: Whether explicit signed actuator channels outperform treating asymmetry as generic dynamics noise.

## 97. AdaClearGrasp: Learning Adaptive Clearing for Zero-Shot Robust Dexterous Grasping in Densely Cluttered Environments (2026) -- Zixuan Chen; Wenquan Zhang; Jing Fang; Ruiming Zeng; Zhixuan Xu; Yiwen Hou; et al.
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 98. Torque Saturation in Bipedal Robotic Walking Through Control Lyapunov Function-Based Quadratic Programs (2015) -- Kevin S. Galloway; Koushil Sreenath; Aaron D. Ames; Jessy W. Grizzle
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 99. A Fault-Tolerant Manipulator Robot Based on ${{\cal H}}_2$, ${{\cal H}}_{\infty }$, and Mixed ${{\cal H}}_2/{{\cal H}}_{\infty }$ Markovian Controls (2009) -- Adriano A. G. Siqueira; M.H. Terra
- Problem claimed: Keep robot performance acceptable when actuators, sensors, or joints fail or degrade.
- Actual mechanism introduced: Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback.
- Hidden assumptions: Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry.
- Variables treated as fixed: Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set.
- Failure modes ignored: Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation.
- What it makes less novel: General claim that actuator nonidealities matter for robot control.
- What it leaves open: How manipulation policy structure should change when positive and negative actuation are unequal but not failed.

## 100. A Collaborative Robotic Approach to Autonomous Pallet Jack Transportation and Positioning (2020) -- Pietro Balatti; Fabio Fusaro; Nicola Villa; Edoardo Lamon; Arash Ajoudani
- Problem claimed: Control manipulators while respecting torque, velocity, or input constraints.
- Actual mechanism introduced: Constrained optimization, model predictive control, anti-windup, or control allocation.
- Hidden assumptions: Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate.
- Variables treated as fixed: Actuator coordinates, contact primitive set, and sign-specific effort margins.
- Failure modes ignored: Directional limits that make one branch/contact primitive safer than another for the same object motion.
- What it makes less novel: Novelty of merely adding actuator limits to a controller.
- What it leaves open: A policy representation where signed actuation cones choose the manipulation primitive itself.
