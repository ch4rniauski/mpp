using System.Text;
using System.Text.Json;
using Microsoft.AspNetCore.Mvc;

namespace prac2.Controllers;

[ApiController]
[Route("")]
public sealed class DownloadController : ControllerBase
{
    private static readonly JsonSerializerOptions JsonOptions = new()
    {
        WriteIndented = true
    };
    
    [HttpGet]
    public IActionResult GetJsonFile()
    {
        var person = new Person("Yauheni", 19);

        var json = JsonSerializer.Serialize(person, JsonOptions);

        var bytes = Encoding.UTF8.GetBytes(json);

        const string fileName = "person.json";
        const string contentType = "application/json";

        return File(bytes, contentType, fileName);
    }
}

internal sealed record Person(string Name, int Age);
