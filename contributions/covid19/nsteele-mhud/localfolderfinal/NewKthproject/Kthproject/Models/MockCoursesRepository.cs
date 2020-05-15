using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Kthproject.Models
{
    public class MockCoursesRepository : ICoursesRepository
    {
        private List<Courses> _coursesList;

        public MockCoursesRepository()
        {
            _coursesList = new List<Courses>()
            {
                new Courses() {Id =1, Name = "Master's programme in Architectural Lighting Design", Department = Dept.SchoolArchitecture,
                    Description = "There is an increasing understanding of the importance of good lighting design in urban areas, " +
                    "buildings and interiors. Light is fundamental to architecture and essential for human well-being. Its quality affects " +
                    "human behaviour, comfort, health, efficiency, safety and security. The programme is based on a new approach to light " +
                    "and light planning – a combination of visual, physical and biological-based experience and knowledge applied to design, " +
                    "technology and health.",Email = "info@kth.se", LinkToCanvus = "http://kth.instructure.com/courses/",
                    PhotoPath = "~/images/MasterArchitecturalLightingDesign.png"},
                new Courses() {Id =2, Name = "Master's programme in Architecture", Department = Dept.SchoolArchitecture,
                    Description = "The master’s programme in Architecture consists of two years of full-time study. The students have the opportunity to choose between a wide range of studio themes that addresses contemporary architectural issues. There is a possibility to develop everything from large scale urban strategies to full scale manufacturing processes. The students will also participate in seminar courses related to specific topics related to ongoing research at the KTH.",Email = "info@kth.se",
                    PhotoPath = "~/images/MasterprogrammeArchitecture.jpg"},
                new Courses() {Id =3, Name = "Master's programme in Chemical Engineering for Energy and Environment",
                    Department = Dept.SchoolEnginneringScience,
                    Description = "The master’s programme in Chemical Engineering for Energy and Environment offer students " +
                    "a comprehensive education in the diverse field of chemical engineering with an emphasis on sustainability. " +
                    "Graduates will possess the engineering tools necessary to meet the future challenge of how best to use the " +
                    "available energy and finite natural resources.",Email = "info@kth.se",
                    PhotoPath = "~/images/MasterChemical Engineering.jpg"},
                new Courses() {Id =4, Name = "Master's programme in Industrial and Environmental Biotechnology",
                    Department = Dept.SchoolEnginneringScience, Description = "The master’s programme in Industrial and " +
                    "Environmental Biotechnology aims to provide deep understanding of how to design and " +
                    "operate state-of-the-art life science based processes, with respect to product quality, " +
                    "sustainability and finance. The goal is to acquire competencies and skills to use cells and cell " +
                    "components such as enzymes to produce commodities such as food, biofuel and biomaterials, for the " +
                    "development of a sustainable society.",Email = "info@kth.se",
                    PhotoPath = "~/images/MasterIndustrialEnvironmental.jpg"},
                new Courses() {Id =5, Name = "Master's programme in Software Engineering of Distributed Systems", Department = Dept.SchoolComputerSecience,
                    Description = "Emerging computer networks and communication technology provide a new technological " +
                    "foundation for designing software systems. The systems become distributed, reconfigurable and adaptive, " +
                    "and their components employ a high degree of autonomy. This is an exciting and rapidly evolving field in" +
                    " which there is a continuous demand for qualified software engineers on the world labour market.",
                    Email = "info@kth.se", PhotoPath = "~/images/MasterSoftwareEngineering.jpg"},
                new Courses() {Id =6, Name = "Master's programme in Systems, Control and Robotics", Department = Dept.SchoolComputerSecience,
                    Description = "The master’s programme in Systems, Control and Robotics equips students with the skills " +
                    "necessary to analyse, design and control complex technical systems such as robots, autonomous vehicles " +
                    "or any other system that has a significant autonomous capability. These systems are important today and " +
                    "will become even more important as new technology makes its way into our workplaces, homes and shared " +
                    "public spaces.",Email = "info@kth.se", PhotoPath = "~/images/MasterprogrammeControlRobotics.jpg"},
                new Courses() {Id =7, Name = "Master's programme in Electromagnetics, Fusion and Space Engineering", Department = Dept.SchoolElectrical,
                    Description = "The two-year master’s programme in Electromagnetics, Fusion and Space Engineering incorporates a strong foundation in electrical engineering with an understanding of electromagnetic fields and how they interact with matter.",Email = "info@kth.se", PhotoPath = "~/images/MasterElectromagneticsEngineering.jpg"},
                new Courses() {Id =8, Name = "Master's programme in Embedded Systems", Department = Dept.SchoolElectrical,
                    Description = "Embedded systems are the most common form of computer system, utilising around 98 percent of all manufactured processors for their applications – from sewing machines and cars, to satellites and power plants. The common denominator for these systems is high-level demands on functionality and reliability. The master’s programme in Embedded Systems foster highly competitive graduates in this important field.",Email = "info@kth.se", PhotoPath = "~/images/MasterprogrammeEmbeddedSystems.jpg"},
                new Courses() {Id =9, Name = "Master's programme in Decentralized Smart Energy Systems (DENSYS)", Department = Dept.SchoolIddustrial,
                    Description = "Decentralized smart energy systems play an increasing role in the perspective of renewable energy sources integration in the energy system and transition towards a low carbon society. After completing this programme, the achieved learning outcome will be a holistic overview on decentralized energy systems and specialized competences in energy engineering.",Email = "info@kth.se", PhotoPath = "~/images/MasterDecentralizedSystems.jpg"},
                new Courses() {Id =10, Name = "Master's programme in Innovative Sustainable Energy Engineering", Department = Dept.SchoolIddustrial,
                    Description = "The joint master's programme in Innovative Sustainable Energy Engineering pools the facilities, innovation and talent from energy departments at the largest technical universities in Sweden, Denmark, Norway, Finland and Iceland.",Email = "info@kth.se", PhotoPath = "~/images/MasterInnovativeSustainable.jpg"},
                new Courses() {Id =1, Name = "Master's programme in Nuclear Energy Engineering", Department = Dept.SchoolEnginneringScience,
                    Description = "The master’s programme in Nuclear Energy Engineering provides you with outstanding career opportunities " +
                    "and excellent opportunities for doctoral studies all over the world. After graduation you can pursue careers as: " +
                    "nuclear engineer (design, development and operation of nuclear power plants), consultant or analyst (nuclear reactor " +
                    "safety, operation and computation support), researcher (development of new generation of reactors) and manager " +
                    "(leadership roles at power plants and nuclear facilities).",Email = "info@kth.se",
                    PhotoPath = "~/images/MasterNuclearEnergyEngineering.jpg"},
            };
        }

        public IEnumerable<Courses> GetAllCourses()
        {
            return _coursesList;
        }
    }
}
