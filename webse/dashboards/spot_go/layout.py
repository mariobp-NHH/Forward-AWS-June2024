html_layout ="""
    <!DOCTYPE html>
    <html>
        <head>
            {%metas%}
              <title>Forward, Spot-GO market</title>
            {%favicon%}
            {%css%}
            
            <meta charset="UTF-8" />
            <meta http-equiv="X-UA-Compatible" content="IE=edge" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />

            <!-- Import Font Awesome CDN. It does not work-->
            <link rel="stylesheet" href="path/to/font-awesome/css/font-awesome.min.css">

            <!-- Import Font Awesome. My own KIT-->
            <script src="https://kit.fontawesome.com/b6331c8bf2.js" crossorigin="anonymous"></script>
            
        </head>
        
        <body>

            <nav class="navbar_spot_go">
            <div class="container_spot_go"> 
                <div class="menu_left">
                    <div class="logo">
                        <a href="/"><img
                            src="/static/figures/forward/forward_icon.svg"
                            width="50" 
                            height="50"
                        alt=""/></a>
                        <a href="/sustainable_energy_platform"><img
                            src="/static/figures/forward/se_platform_icon.svg"
                            width="50" 
                            height="50"
                        alt=""/></a>
                    </div>
                    <div class="menu">
                        <ul class="nav">
                            <li class="nav-item">
                                <a href="/spot_go/">App-Paper</a> 
                            </li>
                            <li class="nav-item">
                                <a href="/papers/spot_go/chat">Chat</a> 
                            </li>
                            <li class="nav-item">
                                <a href="/papers/spot_go/students_questions">Students-Questions</a> 
                            </li>
                            <li class="nav-item">
                                <a href="/papers/spot_go/students_answers">Students-Answers</a> 
                            </li>
                            <li class="nav-item">
                                <a href="/papers/spot_go/calendar">Calendar</a> 
                            </li>
                            <li class="nav-item">
                                <a href="/papers/spot_go/authors">Authors</a> 
                            </li>
                        </ul>  
                    </div>                    
                </div>


                <div class="hamburger">
                    <span class="bar"></span>
                    <span class="bar"></span>
                    <span class="bar"></span>
                </div>
            </div>
        </nav>



            
                <section>
                    <header class="header_css_spot_go">
                        <div class="container">
                            <div class="d-sm-flex align-items-center justify-content-between">
                              <div class="col-lg-7 col-md-7 col-sm-6 col-12">
                                <h1><span class="text-warning"> Spot - Guarantees of Origin App</span></h1>
                                <p, style="font-size: 14px;" style="color: #000000;">Consumers, governments and corporations are becoming more aware of the origin of the energy that they consume, 
                                and the guarantees of origin (GO) market is increasing in Europe and worldwide. <strong>More than 25% of the electricity 
                                consumed in Europe is consumed by using GO markets. </strong>
                                </br>
                                </br>
                                We work out the <strong>subgame perfect Nash equilibrium</strong> when the spot and the GO markets operate sequentially, and different market 
                                designs are implemented in the GO market. 
                                </br>
                                </br>
                                We find that the introduction of GO market could have a <strong>pro-competitive effect</strong> in the spot market. 
                                Moreover, the change on prices in the spot market induced by the introduction of a GO market could <strong>reverse the 
                                flow of electricity</strong> between nodes in the spot market.
                                </p>
                                <div class="container_buttons_links_header">
                                    <div class="btn">
                                        <a href="#"  data-toggle="modal" data-target="#paper_Modal" class="btn btn-primary btn-lg mr-2", style="background-color:#007bff;"><i class="fa-regular fa-newspaper"></i> Paper</a>
                                    </div>
                                    <div class="btn">
                                        <a href="https://xd.adobe.com/view/b2665b34-2dbe-4123-b4ac-64a29748a86c-e735/"  target="_blank" class="btn btn-primary btn-lg mr-2", style="background-color:#007bff;"><i class="fa-solid fa-person-chalkboard"></i> Presentation</a>
                                    </div>
                                </div> 
                              </div>
                              <div class="col-lg-4 col-md-4 col-sm-5 col-12">                                  
                                  <img src="/static/figures/dashboards/spot-go/spot_go_icon.svg" />
                              </div>  
                            </div>

                                <!-- Modal -->
                                <div class="modal fade" id="paper_Modal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                                <div class="modal-dialog modal-lg " style="height: 80%;" >
                                <div class="modal-content" style="height:100%">
                                    <div class="modal-header">
                                    <h5 class="modal-title" id="exampleModalLabel">Paper</h5>
                                    <button type="button" class="btn-close" data-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <div class="modal-body">
                                        <iframe id="paper_frame" src="/static/papers/spot_go/spot_go.pdf" width="100%" height="100%"></iframe>  <!-- Using iframe to view the pdf file.-->
                                    </div>
                                    <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                                    </div>
                                </div>
                                </div>
                                </div> 

                        </div>
                    </header>
                </section>
            {%app_entry%}
            
                 
            
            <footer class="footer_spot_go">
                <div class="container">  
                    <div class="item">
                        <p class="lead">
                        Spot-GO paper
                        </p> 
                    </div>              
                    <div class="item">
                        <a href="#">
                            <i class="bi bi-arrow-up-circle h1"></i>
                        </a>
                    </div> 
                </div>


                {%config%}
                {%scripts%}
                    <script type="text/x-mathjax-config">
                    MathJax.Hub.Config({
                        tex2jax: {
                        inlineMath: [ ['$','$'],],
                        processEscapes: true
                        }
                    });
                    </script>
                {%renderer%}
            </footer>

        
            <!-- Optional JavaScript -->
            <!-- jQuery first, then Popper.js, then Bootstrap JS -->
            <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

        </body>
    </html>
    """
