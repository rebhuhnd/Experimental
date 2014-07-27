public class Worker extends Thread

{
	private String name;

	public Worker(String name){
		this.name = name;
	}

	public void run()
	{
		this.DoStuff();
	}

	public void DoStuff()
	{
		for (int i=0; i<100; i++){
			//Thread.sleep(500);
			System.out.printf("%s says 'Hello'!\n",this.name);
		}
	}
}