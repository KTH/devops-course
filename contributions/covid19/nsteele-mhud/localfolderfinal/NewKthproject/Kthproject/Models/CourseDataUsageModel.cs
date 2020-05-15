using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using static Kthproject.Models.Courses;

namespace Kthproject.Models
{
    public class CourseDataUsageModel : Courses
    {
        private readonly ICoursesRepository coursesRepository;
        public IEnumerable<Courses>Courses { get; set; }
        public CourseDataUsageModel(ICoursesRepository coursesRepository)
        {
            this.coursesRepository = coursesRepository;
        }
        public void OnGet()
        {
            Courses = coursesRepository.GetAllCourses();
        }
    }
}
