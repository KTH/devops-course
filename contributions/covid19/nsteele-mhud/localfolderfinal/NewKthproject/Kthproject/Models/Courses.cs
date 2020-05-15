using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Kthproject.Models
{
    public class Courses
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Description { get; set; }
        public string Email { get; set; }
        public string PhotoPath { get; set; }
        public string LinkToCanvus { get; set; }
        public Dept? Department { get; set; }

    }
}
