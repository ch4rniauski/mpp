namespace prac1._3;

public partial class Form1 : Form
{
    private readonly HttpClient _httpClient = new();

    public Form1()
    {
        InitializeComponent();
    }

    private async void button1_Click(object sender, EventArgs e)
    {
        try
        {
            button1.Enabled = false;
            button1.Text = "Loading";

            var imageBytes = await _httpClient.GetByteArrayAsync("http://localhost:5189/image.jpg");
            using var ms = new MemoryStream(imageBytes);
            pictureBox1.Image = Image.FromStream(ms);
        }
        catch (Exception ex)
        {
            MessageBox.Show($"Error: {ex.Message}");
        }
        finally
        {
            button1.Enabled = true;
            button1.Text = "Load image";
        }
    }
}