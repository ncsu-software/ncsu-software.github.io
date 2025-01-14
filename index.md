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
        .scrollable-div {
            height: 600px; /* Set your preferred height here */
            overflow-y: scroll; /* Enable vertical scrolling */
        }

        /* Set the width of the container */
        .container {
            width: 90%;
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
        <!-- News Section -->
        <h1>News</h1>
        <div class="segment">
            <div class="scrollable-div">    
                <ul>
                <li>
                        <span class="date">10/2024</span>, <strong>Dr. Tim Menzies won ACM SIGSOFT Distinguished Reviewer Award!</strong>
                        <ul>
                            <img src="images/photos/tim-reviewer-award.jpg" alt="Text and Image" style="width: 800px;">
                            <br>
                            Excellent Dr. Tim Menzies! High quality reviews show great respect to hard work!<a href="https://conf.researchr.org/info/ase-2024/awards">Source</a> 
                        </ul>
                    </li>
                    <br>    
                <li>
                        <span class="date">10/2024</span>, <strong>Hiking event during fall break!</strong>
                        <ul>
                            <img src="images/photos/hiking.jpeg" alt="Text and Image" style="width: 800px;"><br>
                            10k steps accomplishment achieved!
                        </ul>
                    </li>
                    <br>
                <li>
                        <span class="date">07/2024</span>, <strong>Dr. Wesley K. G. Assunção won SIGSOFT Distinguished Paper Award at FSE 2024!</strong>
                        <ul>
                            <img src="images/photos/wesley-award.jpeg" alt="Text and Image" style="width: 800px;"><br>
                            Congratulations to Dr. Wesley K. G. Assunção! The paper is titled <i>Understanding Developers' Discussions and Perceptions on Non-Functional Requirements: The Case of the Spring Ecosystem</i> at 32nd International Conference on the Foundations of Software Engineering (FSE) <a href="https://andersonjso.github.io/preprints/fse24oliveira.pdf">More Details</a>
                        </ul>
                    </li>
                    <br>
                    <li>
                        <span class="date">04/2024</span>, <strong>Our student Justin Middleton (supervised by Dr. John-Paul Ore and Dr. Kathryn Stolee) presented a paper at ICSE 2024!</strong>
                        <ul>
                            <img src="images/justin.jpeg" alt="team" style="width: 800px;"><br>
                            Congratulations to our student Justin Middleton! The paper is titled <i>Barriers for Students During Code Change Comprehension</i> at IEEE/ACM 46th International Conference on Software Engineering <a href="https://dl.acm.org/doi/abs/10.1145/3597503.3639227">More Details</a>
                        </ul>
                    </li>
                    <br>
                    <li>
                        <span class="date">04/2024</span>, <strong>Team has fun at ICSE 2024!</strong>
                        <ul>
                            <img src="images/icse.jpeg" alt="team" style="width: 800px;">
                        </ul>
                    </li>
                    <br>
                    <li>
                        <span class="date">03/2024</span>, <strong>Dr. Wesley K. G. Assunção won Distinguished Paper Award!</strong>
                        <ul>
                            <img src="images/wesley-paper-award.jpeg" alt="Text and Image" style="width: 800px;">
                            <br>
                            Excellent Dr. Wesley K. G. Assunção! The awarded work is titled <i>Exploring Dependencies Among Inconsistencies to Enhance the Consistency Maintenance of Models</i>. <a href="https://wesleyklewerton.github.io/publications/SANER24.pdf">Paper</a> 
                        </ul>
                    </li>
                    <br>
                    <li>
                        <span class="date">12/2023</span>, <strong>Dr. Sandeep Kuttal gave an ACM TechTalk!</strong>
                        <ul>
                            <img src="images/photos/sandeep-acm-talk.png" alt="Text and Image" style="width: 800px;">
                            <br>
                            Great job from Dr. Sandeep Kuttal! The talk is titled <i>Towards Seamless Collaboration: Redefining Human-AI Interaction in Programming</i>. <a href="https://events.zoom.us/ejl/AsffhYrgkZXeKDjiW-zn04TPNkI3O1eUffiGu7CLObljJmEsCkFQ~A-g0TO_W9WO_ys4C-TjCOW0v2Y4npevpX-kb25MXKCU1vfxmwD-d7gz1JgRFxdORv89-xkUG8RYipelsEjEk-cKf7Hjn-RQ/home">Video</a> 
                        </ul>
                    </li>
                    <br>
                    <li>
                        <span class="date">10/2023</span>, <strong>Team work on PhD in SE Recruiting Event!</strong>
                        <ul>
                            <img src="images/phd-hire.jpg" alt="Text and Image" style="width: 800px;">
                            <br>
                            We are actively looking for brilliant minds to join us to dream the future of SE and make it happen. Join Software Engineering at NCSU, We Want YOU For Grad School! <a href="https://docs.google.com/presentation/d/e/2PACX-1vQ1hO-ENY6xTgjz-QklVUK4PItG1qx-Ex56D5B2rzP-moNYbkSYuVQOY3Xjv4NpcMlrXflw2Wnci8HP/pub?start=false&loop=false&delayms=3000">Slides</a>
                             <a href="https://ncsu.software/services/students/">More Details</a> 
                        </ul>
                    </li>
                    <br>
                    <li>
                        <span class="date">10/2023</span>, <strong>Dr. Marcelo D'Amorim is serving FSE 2024 as the General Chair!</strong>
                        <ul>
                            Please consider participate the <i>ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering</i> (ESEC/FSE)! See you at Porto de Galinhas, Brazil! <a href="https://2024.esec-fse.org/">More Details</a>
                        </ul>
                    </li>
                    <br>
                    <li>
                        <span class="date">10/2023</span>, <strong>Dr. Sandeep Kuttal gave a keynote at SCAM and VISSOFT 2023!</strong>
                        <ul>
                            Great job from Dr. Sandeep Kuttal! The talk is titled <i>IDEs as the Bridge: Connecting Humans and Code</i> at the IEEE International Working Conference on Source Code Analysis &amp; Manipulation (SCAM) and on Software Visualization (VISSOFT). Bogotá, Colombia, October 2023. <a href="https://sandeepkuttal.github.io/kuttal/index.html">More Details</a>
                        </ul>
                    </li>
                    <br>
                    <li>
                        <span class="date">10/2023</span>, <strong>Our student Shandler A. Mason (supervised by Dr. Sandeep Kuttal) presented a paper at VLHCC 2023!</strong>
                        <ul>
                            Congratulations to our student Shandler A. Mason! The paper is titled <i>Investigating Interracial Pair Coordination During Remote Pair Programming</i> at IEEE Symposium on Visual Languages and Human-Centric Computing (VLHCC). Washington, DC, USA. <a href="https://sandeepkuttal.github.io/kuttal/index.html">More Details</a>
                        </ul>
                    </li>
                    <br>
                    <li>
                        <span class="date">10/2023</span>, <strong>Our student Leon Shahnewaz (supervised by Dr. Sandeep Kuttal) presented a paper at VLHCC 2023!</strong>
                        <ul>
                            Congratulations to our students Leon Shahnewaz, Mahzabin Tamanna, and Dr. Sandeep Kuttal! The paper is titled <i>Comparing Foraging Behavior Across Code Hosting and Q&amp;A Platforms through a Gender Lens</i> at IEEE Symposium on Visual Languages and Human-Centric Computing (VLHCC). Washington, DC, USA. <a href="https://sandeepkuttal.github.io/kuttal/index.html">More Details</a>
                        </ul>
                    </li>
                    <br>
                    <li>
                        <span class="date">09/2023</span>, <strong>Dr. Tim Menzies was designated ASE Fellow!</strong>
                        <ul>
                            Congratulations to Dr. Tim Menzies! He was designated a Fellow of Automated Software Engineering at the 38th IEEE/ACM International Conference on Automated Software Engineering (ASE). <a href="https://timm.fyi/">More Details</a>
                        </ul>
                    </li>
                    <br>
                    <li>
                        <span class="date">09/2023</span>, <strong>Dr. Wesley K. G. Assunção Won Best Paper Award at SPLC 2023!</strong>
                        <ul>
                            Congratulations to Dr. Wesley K. G. Assunção and his co-authors from the Federal University of Paraná, on recently winning the Best Research Paper award at the 27th ACM International Systems and Software Product Line Conference (SPLC). <a href="https://wesleyklewerton.github.io/">More Details</a>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</body>