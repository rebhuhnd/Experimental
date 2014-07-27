public class WorkerTest
{
	public static void main(String args[]) throws Exception{
		Worker b = new Worker("Bob");
		Worker s = new Worker("Sally");
		Worker j = new Worker("Jerry");

//		b.DoStuff();
//		s.DoStuff();
//		j.DoStuff();

		b.start();
		s.start();
		j.start();

	}
}