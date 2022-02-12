using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace ift_402_project.Controllers
{
    [Authorize]
    public class DashboardController : Controller
    {
        public ActionResult Index()
        {
            return View();
        }

        public ActionResult Alerts()
        {
            return View();
        }

        public ActionResult Queries()
        {
            return View();
        }

        public ActionResult Scans()
        {
            return View();
        }

        public ActionResult ScanDetails()
        {
            return View();
        }

        public ActionResult QueryDetails()
        {
            return View();
        }
    }
}
