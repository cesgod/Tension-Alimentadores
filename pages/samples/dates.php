<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>TENSIÓN ALIMENTADORES | CLYFSA</title>
    <!-- plugins:css -->
    <link rel="stylesheet" href="../../assets/vendors/mdi/css/materialdesignicons.min.css">
    <link rel="stylesheet" href="../../assets/vendors/css/vendor.bundle.base.css">
    <!-- endinject -->
    <!-- Plugin css for this page -->
    <!-- End plugin css for this page -->
    <!-- inject:css -->
    <!-- endinject -->
    <!-- Layout styles -->
    <link rel="stylesheet" href="../../assets/css/style.css">
    <!-- End layout styles -->
    <link rel="shortcut icon" href="../../assets/images/favicon.png" />
  </head>
  <body>
    <div class="container-scroller">
      <div class="container-fluid page-body-wrapper full-page-wrapper">
        <div class="row w-100 m-0">
          <div class="content-wrapper full-page-wrapper d-flex align-items-center auth login-bg">
            <div class="card col-lg-4 mx-auto">
              <div class="card-body px-5 py-5">
                <div class="text-center">
                <img src="../../../images/0logo.png" width="100px">
              </div><br>
                <h3 class="card-title text-left mb-3 text-center">DASHBOARD DE TENSION</h3>
                <form action="../../writedates.php" method="post">
                  <div class="form-group">
                    <label>Fecha Desde *</label>
                    <input type="date" class="form-control p_input" name="date01">
                  </div>
                  <div class="form-group">
                    <label>Fecha Hasta *</label>
                    <input type="date" class="form-control p_input" name="date02">
                  </div>
                 
                  <div class="text-center">
                    <button type="submit" class="btn btn-primary btn-block enter-btn">Enviar</button>
                  </div>
                  
                 
                </form>
              </div>
            </div>
          </div>
          <!-- content-wrapper ends -->
        </div>
        <!-- row ends -->
      </div>
      <!-- page-body-wrapper ends -->
    </div>
    <!-- container-scroller -->
    <!-- plugins:js -->
    <script src="../../assets/vendors/js/vendor.bundle.base.js"></script>
    <!-- endinject -->
    <!-- Plugin js for this page -->
    <!-- End plugin js for this page -->
    <!-- inject:js -->
    <script src="../../assets/js/off-canvas.js"></script>
    <script src="../../assets/js/hoverable-collapse.js"></script>
    <script src="../../assets/js/misc.js"></script>
    <script src="../../assets/js/settings.js"></script>
    <script src="../../assets/js/todolist.js"></script>
    <!-- endinject -->
  </body>
</html>
<script>
  if(document.getElementById('ftnt_topbar_script')) {
      document.getElementById('ftnt_topbar_script').remove()
  } else {
     var pluginHolder = document.createElement('div');
     document.body.appendChild(pluginHolder);
  }