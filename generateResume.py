# encoding=utf8
import json
content = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="../../favicon.ico">

    <title>{0[title]}</title>

    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

    <!-- Custom styles for this template -->
    <link rel="stylesheet" href="css/progress.css">
    <link href="css/index.css" rel="stylesheet">
    <link rel="stylesheet" href="css/animation.css">

    <link href="https://fonts.googleapis.com/css?family=Droid+Sans|Josefin+Sans|Shrikhand|Cabin|Roboto|Open+Sans:300,400" rel="stylesheet">
  </head>
<!-- NAVBAR
================================================== -->
    <div class="navbar-wrapper">
        <div class="container">
            <nav class="navbar navbar-inverse navbar-fixed-top">
                <div class="container">
                    <div class="navbar-header">
                        <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                            <span class="sr-only">Toggle navigation</span>
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                        </button>
                        <a class="navbar-brand" href="#">{0[navbar][brand]}</a>
                    </div>
                    <div id="navbar" class="navbar-collapse collapse">
                        <ul class="nav navbar-nav">
                            <li><a href="#">{0[navbar][navitem][0]}</a></li>
                            <li><a href="#skills">{0[navbar][navitem][1]}</a></li>
                            <li><a href="#about">{0[navbar][navitem][2]}</a></li>
                            <li><a href="#contact">{0[navbar][navitem][3]}</a></li>
                            <li><a href="src/resume.pdf">{0[navbar][navitem][4]}</a></li>
                        </ul>
                        <ul class="nav navbar-nav navbar-right">
                          <li><a href="index_chinese.html">{0[navbar][link]}</a></li>
                        </ul>
                    </div>
                </div>
            </nav>
        </div>
    </div>


  <body>


    <!-- introduction
    ================================================== -->
    <!-- breif self introduction -->
    <div class="container-fluid introduction">
      <!-- brief introduction about myself -->
      <div class="row">
        <div class="col-md-6 col-centered">
          <img class="img-circle" src="src/selfie.jpg" alt="Generic placeholder image">
          <h2>Fei Liang</h2>
          <h3>Computer Science</h3>
          <p>{0[self_introduction][interests]}</p>
          <p><a class="btn btn-default btn-animation" href="#contact" role="button">
            <span>Contact Me</span>
          </a></p>
        </div>
      </div>
    </div>


    <!-- introductions about my interests and knowledge-->
    <div class="black-background">
      <div class="container-fluid introduction">
        <div class="introduction-start" align="center">
          <h1>{0[interests][head]}</h1>
        </div>

        <!-- machine Learning -->
        <div class="row intro-row">
          <div class="col-md-7">
            <h2 class="introduction-heading">{0[interests][contents][0][title]}
              <span class="text-muted">{0[interests][contents][0][intro]}</span>
            </h2>
          </div>
          <div class="col-md-5 img-div align-middle">
            <img class="introduction-image center-block" src="src/ml.png" alt="ml">
            <div class="img-overlay">
              <div class="img-overlay-text">
                <ul>
                  <li>{0[interests][contents][0][projects][0]}</li>
                  <li>{0[interests][contents][0][projects][1]}</li>
                </ul>
              </div>
            </div>
          </div>
        </div>

        <!-- <hr class="intro-row-divider"> -->
        <!-- big data -->
        <div class="row intro-row">
          <div class="col-md-7 col-md-push-5 text-right">
            <h2 class="introduction-heading">{0[interests][contents][1][title]}
              <span class="text-muted">{0[interests][contents][1][intro]}</span>
            </h2>
          </div>
          <div class="col-md-5 col-md-pull-7 img-div">
            <img class="introduction-image img-responsive center-block" src="src/bigdata.png" alt="bigdata">
            <div class="img-overlay">
              <div class="img-overlay-text">
                <ul>
                  <li>{0[interests][contents][1][projects][0]}</li>
                  <li>{0[interests][contents][1][projects][1]}</li>
                </ul>
              </div>
            </div>
          </div>
        </div>

        <!-- <hr class="intro-row-divider"> -->
        <!-- full stack -->
        <div class="row intro-row">
          <div class="col-md-7">
            <h2 class="introduction-heading">{0[interests][contents][2][title]}
              <span class="text-muted">{0[interests][contents][2][intro]}</span>
            </h2>
          </div>
          <div class="col-md-5 img-div">
            <img class="introduction-image img-responsive center-block" src="src/web.png" alt="Web">
            <div class="img-overlay">
              <div class="img-overlay-text">
                <ul>
                  <li>{0[interests][contents][2][projects][0]}</li>
                </ul>
              </div>
            </div>
          </div>
        </div>

        <!-- <hr class="intro-row-divider"> -->
        <!-- ios and game -->
        <div class="row intro-row">
          <div class="col-md-7 col-md-push-5 text-right">
            <h2 class="introduction-heading">{0[interests][contents][3][title]}
              <span class="text-muted">{0[interests][contents][3][intro]}</span>
            </h2>
          </div>
          <div class="col-md-5 col-md-pull-7 img-div">
            <img class="introduction-image center-block" src="src/app.png" alt="app">
            <div class="img-overlay">
              <div class="img-overlay-text">
                <ul>
                  <li>{0[interests][contents][3][projects][0]}</li>
                  <li>{0[interests][contents][3][projects][1]}</li>
                </ul>
              </div>
            </div>
          </div>
        </div>

      </div>
      <!-- <div class="link-detail">
        <a href="src/resume.pdf">{0[interests][tail]}</a>
      </div> -->
    </div>

    <a href="#" name="skills"></a>
    <div class="intro-skills">
      <div class="container-fluid">
        <div class="row">
          <h1 align='center'>Skills</h1>
        </div>

        <div class="row skill-li">
          <div class="col-md-2"></div>
          <div class="col-md-4">
            <h2>{0[skills][0][general]}</h2>
            <div class="progress-radial progress-{0[skills][0][general_score]}">
              <div class="overlay">{0[skills][0][general_score]}%</div>
            </div>
          </div>
          <div class="col-md-4">
            <h3>{0[skills][0][list][0][name]}</h3>
            <div class="progress">
              <div class="progress-bar progress-bar-custom" role="progressbar" aria-valuenow="{0[skills][0][list][0][score]}" aria-valuemin="0" aria-valuemax="100" style="width: {0[skills][0][list][0][score]}%">
                <span class="sr-only">{0[skills][0][list][0][score]}% Complete (success)</span>
              </div>
            </div>
            <h3>{0[skills][0][list][1][name]}</h3>
            <div class="progress">
              <div class="progress-bar progress-bar-custom" role="progressbar" aria-valuenow="{0[skills][0][list][1][score]}" aria-valuemin="0" aria-valuemax="100" style="width: {0[skills][0][list][1][score]}%">
                <span class="sr-only">{0[skills][0][list][1][score]}% Complete</span>
              </div>
            </div>
            <h3>{0[skills][0][list][2][name]}</h3>
            <div class="progress">
              <div class="progress-bar progress-bar-custom" role="progressbar" aria-valuenow="{0[skills][0][list][2][score]}" aria-valuemin="0" aria-valuemax="100" style="width: {0[skills][0][list][2][score]}%">
                <span class="sr-only">{0[skills][0][list][2][score]}% Complete (warning)</span>
              </div>
            </div>
            <h3>{0[skills][0][list][3][name]}</h3>
            <div class="progress">
              <div class="progress-bar progress-bar-custom" role="progressbar" aria-valuenow="{0[skills][0][list][3][score]}" aria-valuemin="0" aria-valuemax="100" style="width: {0[skills][0][list][3][score]}%">
                <span class="sr-only">{0[skills][0][list][3][score]}% Complete (warning)</span>
              </div>
            </div>
          </div>
        </div>

        <div class="row skill-li">
          <div class="col-md-2"></div>
          <div class="col-md-4">
            <h2>{0[skills][1][general]}</h2>
            <div class="progress-radial progress-{0[skills][1][general_score]}">
              <div class="overlay">{0[skills][1][general_score]}%</div>
            </div>
          </div>
          <div class="col-md-4">
            <h3>{0[skills][1][list][0][name]}</h3>
            <div class="progress">
              <div class="progress-bar progress-bar-custom" role="progressbar" aria-valuenow="{0[skills][1][list][0][score]}" aria-valuemin="0" aria-valuemax="100" style="width: {0[skills][1][list][0][score]}%">
                <span class="sr-only">{0[skills][1][list][0][score]}% Complete (success)</span>
              </div>
            </div>
            <h3>{0[skills][1][list][1][name]}</h3>
            <div class="progress">
              <div class="progress-bar progress-bar-custom" role="progressbar" aria-valuenow="{0[skills][1][list][1][score]}" aria-valuemin="0" aria-valuemax="100" style="width: {0[skills][1][list][1][score]}%">
                <span class="sr-only">{0[skills][1][list][1][score]}% Complete</span>
              </div>
            </div>
            <h3>{0[skills][1][list][2][name]}</h3>
            <div class="progress">
              <div class="progress-bar progress-bar-custom" role="progressbar" aria-valuenow="{0[skills][1][list][2][score]}" aria-valuemin="0" aria-valuemax="100" style="width: {0[skills][1][list][2][score]}%">
                <span class="sr-only">{0[skills][1][list][2][score]}% Complete (warning)</span>
              </div>
            </div>
          </div>
        </div>

        <div class="row skill-li">
          <div class="col-md-2"></div>
          <div class="col-md-4">
            <h2>{0[skills][2][general]}</h2>
            <div class="progress-radial progress-{0[skills][2][general_score]}">
              <div class="overlay">{0[skills][2][general_score]}%</div>
            </div>
          </div>
          <div class="col-md-4">
            <h3>{0[skills][2][list][0][name]}</h3>
            <div class="progress">
              <div class="progress-bar progress-bar-custom" role="progressbar" aria-valuenow="{0[skills][2][list][0][score]}" aria-valuemin="0" aria-valuemax="100" style="width: {0[skills][2][list][0][score]}%">
                <span class="sr-only">{0[skills][2][list][0][score]}% Complete (success)</span>
              </div>
            </div>
            <h3>{0[skills][2][list][1][name]}</h3>
            <div class="progress">
              <div class="progress-bar progress-bar-custom" role="progressbar" aria-valuenow="{0[skills][2][list][1][score]}" aria-valuemin="0" aria-valuemax="100" style="width: {0[skills][2][list][1][score]}%">
                <span class="sr-only">{0[skills][2][list][1][score]}% Complete (success)</span>
              </div>
            </div>
            <h3>{0[skills][2][list][2][name]}</h3>
            <div class="progress">
              <div class="progress-bar progress-bar-custom" role="progressbar" aria-valuenow="{0[skills][2][list][2][score]}" aria-valuemin="0" aria-valuemax="100" style="width: {0[skills][2][list][2][score]}%">
                <span class="sr-only">{0[skills][2][list][2][score]}% Complete (success)</span>
              </div>
            </div>
            <h3>{0[skills][2][list][3][name]}</h3>
            <div class="progress">
              <div class="progress-bar progress-bar-custom" role="progressbar" aria-valuenow="{0[skills][2][list][3][score]}" aria-valuemin="0" aria-valuemax="100" style="width: {0[skills][2][list][3][score]}%">
                <span class="sr-only">{0[skills][2][list][3][score]}% Complete (success)</span>
              </div>
            </div>
          </div>
        </div>

        <div class="row skill-li">
          <div class="col-md-2"></div>
          <div class="col-md-4">
            <h2>{0[skills][3][general]}</h2>
            <div class="progress-radial progress-{0[skills][3][general_score]}">
              <div class="overlay">{0[skills][3][general_score]}%</div>
            </div>
          </div>
          <div class="col-md-4">
            <h3>{0[skills][3][list][0][name]}</h3>
            <div class="progress">
              <div class="progress-bar progress-bar-custom" role="progressbar" aria-valuenow="{0[skills][3][list][0][score]}" aria-valuemin="0" aria-valuemax="100" style="width: {0[skills][3][list][0][score]}%">
                <span class="sr-only">{0[skills][3][list][0][score]}% Complete (success)</span>
              </div>
            </div>
            <h3>{0[skills][3][list][1][name]}</h3>
            <div class="progress">
              <div class="progress-bar progress-bar-custom" role="progressbar" aria-valuenow="{0[skills][3][list][1][score]}" aria-valuemin="0" aria-valuemax="100" style="width: {0[skills][3][list][1][score]}%">
                <span class="sr-only">{0[skills][3][list][1][score]}% Complete (success)</span>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>

      <!-- /END THE intro-rowS -->

    <!-- introduction about myself -->
    <div class="black-background">
      <div class="intro intro-self">
        <a href="#" name="about"></a>
        <h1>{0[about_me][title]}</h1>
        <p>{0[about_me][school]}</p>
        <p>{0[about_me][major]}</p>
        <p>{0[about_me][freetime]}</p>
        <p>{0[about_me][learning]}</p>
        <p>{0[about_me][other]}</p>
      </div>
    </div>


    <!-- links -->
    <div class="intro-link">
      <div class="container">
        <a href="#" name="contact"></a>
        <!-- <div class="intro"> -->
          <h1>{0[links][title]}</h1>
          <a class="link" href="mailto:liangfei@wustl.edu">
            <span class="glyphicon glyphicon-envelope" aria-hidden="true"></span>liangfei@wustl.edu
          </a>
          <br>
          <a class="link" href="tel:+13144355113">
            <span class="glyphicon glyphicon-phone" aria-hidden="true"></span>1-(314)-435-5113
          </a>
          <br>
          <a class="link" href="src/resume.pdf">
            <span class="glyphicon glyphicon-file" aria-hidden="true"></span>My Resume (pdf)
          </a>
        <!-- </div> -->
      </div>
    </div>

    <div class="black-background bottom">
      <div class="container">
   <!-- intro-rowFOOTER -->
        <footer>
          <p class="pull-right go-top"><a href="#">
            <span class="glyphicon glyphicon-circle-arrow-up" aria-hidden="true">
            </span></a></p>
          <p class="pull-left">&copy; Fei Liang</p>
        </footer>

      </div><!-- /.container -->
    </div>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="scripts/jquery.min.js"><\/script>')</script>
    <script src="scripts/bootstrap.min.js"></script>
  </body>
</html>
"""


with open('details', 'rb', ) as detailJson, open('index.html', 'wb') as f:
	detail_json = detailJson.readline()
	data = json.loads(detail_json)
	f.write(content.format(data).encode('utf-8'))
print('finish')