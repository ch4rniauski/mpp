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

app.UseStaticFiles();

await app.RunAsync();
