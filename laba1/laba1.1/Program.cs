var builder = WebApplication.CreateBuilder(args);

builder.Services.AddCors(opt =>
    opt.AddDefaultPolicy(policy =>
    {
        policy
            .AllowAnyOrigin()
            .AllowAnyHeader()
            .AllowAnyMethod();
    }));

var app = builder.Build();

app.UseCors();

app.MapGet("/", () => new List<ClientDto>
{
    new(Guid.NewGuid(), "person", "Иванов Иван", "AB1234567", "Минск", "+375291111111"),
    new(Guid.NewGuid(), "company", "Рога-Копыта", null, "Гродно", "+375152444444"),
    new(Guid.NewGuid(), "person", "Петров Петр", "AB7654321", "Минск", "+375292222222")
});

await app.RunAsync();

internal record ClientDto(
    Guid Id,
    string ClientType,
    string Name,
    string? Passport,
    string Address,
    string Phone
);
