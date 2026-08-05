from app.services.syntax_checker import SyntaxChecker

python_code = """
def hello():
    print("Hello")
"""

java_code = """
public class Test{
    public static void main(String args[]){
        System.out.println("Hello");
    }
}
"""

print(SyntaxChecker.validate("Python", python_code))
print(SyntaxChecker.validate("Java", java_code))