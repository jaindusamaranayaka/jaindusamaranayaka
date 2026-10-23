<div align="center">

<!-- ========================================== -->
<!-- 1. LIVE ANIMATED CONTRIBUTION HEATMAP      -->
<!-- ========================================== -->

<h3><code>jaindu@moratuwa:~$ ./contributions.sh</code></h3>

<img src="./contrib-heatmap.svg" width="860" alt="Jaindu's GitHub contribution graph — auto-refreshed daily" />

<br>
<br>

<!-- ========================================== -->
<!-- 2. ASCII PORTRAIT + NEOFETCH TERMINAL CARD -->
<!-- ========================================== -->

<h3><code>jaindu@moratuwa:~$ whoami --profile</code></h3>

<table>
  <tr>
    <td valign="top" width="420">
      <img src="./jaindu-ascii.svg" width="420" alt="Jaindu Samaranayaka — Monochrome ASCII Portrait" />
    </td>
    <td valign="top" width="420">
      <img src="./info-card.svg" width="420" alt="Jaindu Samaranayaka — Neofetch Info Card" />
    </td>
  </tr>
</table>

<br>

<!-- Collapsible Live Streak Telemetry -->
<details>
  <summary><b>📈 Click to view GitHub Streak & Monthly Activity Telemetry</b></summary>
  <br>
  <img src="./stats.svg" width="860" alt="Jaindu's Live Streak and Activity Telemetry" />
</details>

<br>
<br>

<!-- Quick Link Action Buttons -->
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jaindu-samaranayake-168782287)
[![Email](https://img.shields.io/badge/Email-devnaka6912%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:devnaka6912@gmail.com)
[![University](https://img.shields.io/badge/Moratuwa-ENTC-800000?style=for-the-badge)](https://ent.uom.lk/)

</div>

<br>

---

### <code>jaindu@moratuwa:~$ cat about_me.txt</code>

```txt
================================================================================
NAME        : Jaindu Samaranayaka
INSTITUTION : University of Moratuwa
DEPARTMENT  : Electronic and Telecommunication Engineering (ENTC)
SPECIALTY   : Bridging Hardware & Software Architecture
================================================================================
```

I am an **Electronic and Telecommunication Engineering undergraduate** at the University of Moratuwa. I specialize in bridging hardware and software, with a strong focus on:
- 🔬 **Digital System Design & ASIC/FPGA Development**: Designing custom RTL in SystemVerilog, synthesis, physical design, and hardware acceleration architectures.
- 🧠 **Computer Vision & Machine Learning**: Building custom CNN image classifiers in Python/TensorFlow and researching stereo/disparity-based depth estimation.
- 💻 **Computer Architecture**: Implementing pipelined & non-pipelined RISC processors from scratch with an open-source EDA flow.
- 🤖 **Robotics & Embedded Systems**: Designing multi-axis robotic arms, PCB layouts (Altium), 3D structural CAD (SolidWorks), and IoT architectures (ESP32, Raspberry Pi).

---

### <code>jaindu@moratuwa:~$ ./list_hardware_and_tools.sh --all</code>

#### ⚡ Hardware, ASIC Flow & CAD
![SystemVerilog](https://img.shields.io/badge/SystemVerilog-00599C?style=for-the-badge)
![Intel Quartus](https://img.shields.io/badge/Intel_Quartus_Prime-0071C5?style=for-the-badge&logo=intel&logoColor=white)
![Yosys](https://img.shields.io/badge/Yosys-2E8B57?style=for-the-badge)
![OpenROAD](https://img.shields.io/badge/OpenROAD-1081C4?style=for-the-badge)
![KLayout](https://img.shields.io/badge/KLayout-005571?style=for-the-badge)
![OpenSCAD](https://img.shields.io/badge/OpenSCAD-F9DF16?style=for-the-badge&logo=openscad&logoColor=black)
![Altium Designer](https://img.shields.io/badge/Altium_Designer-A5CD39?style=for-the-badge&logo=altiumdesigner&logoColor=white)
![SolidWorks](https://img.shields.io/badge/SolidWorks-E32227?style=for-the-badge)
![Raspberry Pi](https://img.shields.io/badge/Raspberry_Pi-A22846?style=for-the-badge&logo=raspberrypi&logoColor=white)

#### 💻 Software, Machine Learning & Infrastructure
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![C++](https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

---

### <code>jaindu@moratuwa:~$ ./featured_projects.sh --details</code>

<table>
<tr>
<td width="50%" valign="top">

#### ⚡ [Pipelined & Non-Pipelined RISC CPU](https://github.com/jaindusamaranayaka/Pipelined--And-Non-pipelined-CPU)
Custom 16-bit RISC-like CPU in SystemVerilog driven through a complete end-to-end open-source ASIC flow:
- **Yosys**: Logic synthesis (RTL to gate-level netlist)
- **OpenROAD**: Placement & Routing, floorplanning, CTS, global/detailed routing, and STA
- **KLayout**: 2D GDSII silicon layout inspection & DRC
- **gds3xtrude + OpenSCAD**: 3D physical IC die rendering

</td>
<td width="50%" valign="top">

#### ⚙️ FPGA CNN Accelerator
Hardware-based Convolutional Neural Network accelerator designed for edge AI inference:
- Custom generic integer multiplier & divider cores
- Generic pipelined matrix multiplication processing elements
- Optimized memory buffering and bandwidth utilization for high-throughput computing

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### 👁️ Computer Vision & ML Pipeline
Deep learning and spatial intelligence research:
- Replicating academic research on disparity-based depth estimation using multi-view stereo image processing
- Developed custom Python/TensorFlow CNN classifiers utilizing regression and classification models

</td>
<td width="50%" valign="top">

#### 🦾 Multi-Axis Robotic Arm Development
End-to-end electro-mechanical robotic arm engineering:
- Structural 3D CAD kinematic modeling in SolidWorks for mechanical linkages
- Actuation and closed-loop position control with embedded microcontrollers
- Power delivery and motor driving circuitry integration

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### 🏥 Automated Patient Monitoring Architecture
- ESP32-based health parameter telemetry built for clinical research environments
- Developed as an entrepreneurial innovation project for the **SPARK Challenge**

</td>
<td width="50%" valign="top">

#### 💧 Smart Digital Water Metering
- Real-time digital liquid flow tracking using a pulse output meter and GSM cellular module
- Telemetry transmitted to an active cloud database deployed on **Railway**

</td>
</tr>
</table>

---

### <code>jaindu@moratuwa:~$ cat community_and_leadership.log</code>

- 🏅 **Program Committee Member & Volunteer** — IEEE Robotics and Automation Society (RAS) Student Branch Chapter.
- 🏁 **Event Organizer** — Successfully organized the national **Maze X Micromouse Competition**, coordinating autonomous maze-solving robotics challenges.

---

### <code>jaindu@moratuwa:~$ ./connect.sh</code>

Feel free to connect or reach out for collaborations in silicon design, embedded systems, or machine learning:

- 💼 **LinkedIn**: [linkedin.com/in/jaindu-samaranayake-168782287](https://www.linkedin.com/in/jaindu-samaranayake-168782287)
- ✉️ **Email**: [devnaka6912@gmail.com](mailto:devnaka6912@gmail.com)
- 🌐 **GitHub**: [@jaindusamaranayaka](https://github.com/jaindusamaranayaka)

<br>

<div align="center">
<sub>Automated SVG telemetry auto-refreshed daily via GitHub Actions ⚙️</sub>
</div>
