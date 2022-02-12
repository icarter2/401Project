using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(ift_402_project.Startup))]
namespace ift_402_project
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }
    }
}
