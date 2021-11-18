using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ift_401project.Controllers
{
    public class DashboardController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }

        public IActionResult Alerts()
        {
            return View();
        }

        public IActionResult Queries()
        {
            return View();
        }

        public IActionResult Scans()
        {
            return View();
        }

        public IActionResult ScanDetails()
        {
            return View();
        }

        public IActionResult QueryDetails()
        {
            return View();
        }
    }
}
