---
title: NC State Software Engineering
layout: home
description: Index PAge Description in index.md
# intro_image: "images/empty.png"
# intro_image: "images/group.jpeg"
intro_image_absolute: false
intro_image_hide_on_mobile: true
show_call_box: false
---

<head>
    <style>

        .news {
            height: 300px;
            overflow: auto;
            width: 90%;
        }

        /* Set the width of the container */
        .container {
            width: 100%;
        }

        /* Set the height of the images */
        img {
            max-width: 100%; /* limit the maximum width of the image */
            height: auto;
        }

        /* Center align the content within each segment */
        .segment {
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;
            padding: 10px 0;
        }

        /* Add some padding between the segments */
        .segment:not(:last-child) {
            margin-right: 16px;
        }

        /* Responsive design adjustments */
        @media screen and (max-width: 768px) {
            .segment {
                flex-direction: column;
            }

            .segment img {
                max-width: 100%;
                width: auto;
                height: auto;
            }

            .segment > div {
                text-align: center;
            }
        }
    </style>
</head>
<body>
    <!-- Container -->
    <div class="container">
        <!-- Image -->
        <div class="segment">
            <img src="images/group.jpeg" alt="Department Image">
        </div>
        <!-- Text and Image -->
        <div class="segment">
            <div>
                <h1>Software Engineering at NCSU</h1>
                <p>Accelerate your SE career, in industry, in research.</p>
            </div>
            <img src="images/illustrations/pointing.svg" alt="Text and Image" style="width: 400px;">
        </div>
    </div>
    <!-- News Section -->
    <div id="news">
            <div>
                <h1>News</h1>
                <ul>
                    <li>
                        <span class="date">10/2023</span>, <strong>Dr. Marcelo D'Amorim is serving FSE 2024 as the General Chair!</strong>
                        <ul>
                            Please consider participate the <i>ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering</i> (ESEC/FSE)! See you at Porto de Galinhas, Brazil! <a href="https://2024.esec-fse.org/">More Details</a>
                        </ul>
                    </li>
                    <li>
                        <span class="date">10/2023</span>, <strong>Dr. Sandeep Kuttal gave a keynote at SCAM and VISSOFT 2023!</strong>
                        <ul>
                            Great job from Dr. Sandeep Kuttal! The talk is titled <i>IDEs as the Bridge: Connecting Humans and Code</i> at the IEEE International Working Conference on Source Code Analysis &amp; Manipulation (SCAM) and on Software Visualization (VISSOFT). Bogotá, Colombia, October 2023. <a href="https://sandeepkuttal.github.io/kuttal/index.html">More Details</a>
                        </ul>
                    </li>
                    <li>
                        <span class="date">10/2023</span>, <strong>Our student Leon Shahnewaz (supervised by Dr. Sandeep Kuttal) presented a paper at VLHCC 2023!</strong>
                        <ul>
                            Congratulations to our students Leon Shahnewaz, Mahzabin Tamanna, and Dr. Sandeep Kuttal! The paper is titled <i>Comparing Foraging Behavior Across Code Hosting and Q&amp;A Platforms through a Gender Lens</i> at IEEE Symposium on Visual Languages and Human-Centric Computing (VLHCC). Washington, DC, USA. <a href="https://sandeepkuttal.github.io/kuttal/index.html">More Details</a>
                        </ul>
                    </li>
                    <li>
                        <span class="date">09/2023</span>, <strong>Dr. Tim Menzies was designated ASE Fellow!</strong>
                        <ul>
                            Congratulations to Dr. Tim Menzies! He was designated a Fellow of Automated Software Engineering at the 38th IEEE/ACM International Conference on Automated Software Engineering (ASE). <a href="https://timm.fyi/">More Details</a>
                        </ul>
                    </li>
                    <li>
                        <span class="date">09/23</span>, <strong>Dr. Wesley K. G. Assunção Won Best Paper Award at SPLC 2023!</strong>
                        <ul>
                            Congratulations to Dr. Wesley K. G. Assunção and his co-authors from the Federal University of Paraná, on recently winning the Best Research Paper award at the 27th ACM International Systems and Software Product Line Conference (SPLC). <a href="https://wesleyklewerton.github.io/">More Details</a>
                        </ul>
                    </li>
                </ul>
            </div>
    </div>
</body>
