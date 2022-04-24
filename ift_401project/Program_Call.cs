
//C# Program Call Segment

using System;
using System.Diagnostics;
namespace ShodanApplication{
   class Program{
      static void Main(){
         Process shodan = new Process();
         shodan.StartInfo.FileName = "python3.exe";
         shodan.StartInfo.Arguments = "MySQL_DB_call <UserEmail> <Hostname or IP address>";
         shodan.Start();
         Console.ReadLine();
      }
   }
}
