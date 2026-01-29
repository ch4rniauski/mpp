using Microsoft.AspNetCore.Mvc;

namespace laba1._1.Controllers;

[ApiController]
[Route("")]
public sealed class ClientsController : ControllerBase
{
    [HttpGet]
    public IList<ClientDto> GetClients()
    {
        return new List<ClientDto>
        {
            new(Guid.NewGuid(), "person", "Иванов Иван", "AB1234567", "Минск", "+375291111111"),
            new(Guid.NewGuid(), "company", "Рога-Копыта", null, "Гродно", "+375152444444"),
            new(Guid.NewGuid(), "person", "Петров Петр", "AB7654321", "Минск", "+375292222222")
        };
    }
}

public sealed record ClientDto(
    Guid Id,
    string ClientType,
    string Name,
    string? Passport,
    string Address,
    string Phone
);