using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;


namespace APIclient
{
  class ShodanAPI
  {
        ///<summary>
    ///   The main entry point for the application
    /// </summary>
    [STAThread]
    public static void Main(string[] args)
    {
      using var ClientAPI = new HttpClient();

      var result = await ClientAPI.GetAsync("https://api.shodan.io");
      Console.WriteLine(result.StatusCode);
    }
  }
}
