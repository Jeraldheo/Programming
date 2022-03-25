

public class GradeBook
{
    private String curseName;
    private String instructorName;

    public GradeBook(String instructor, String curse)
    {
        instructorName = instructor;
        curseName = curse;
    }

    public void setCurseName(String name)
    {
        curseName = name;
    }

    public String getCurseName()
    {
        return curseName;
    }

    public void setInstructorName(String name)
    {
        instructorName = name;
    }

    public String getInstructorName()
    {
        return instructorName;
    }

    public void display_Message()
    {
        System.out.printf("Welcome to the grade book \n%s!\nThis course is presented by: \n%s\n", getCurseName(), getInstructorName());
    }
}