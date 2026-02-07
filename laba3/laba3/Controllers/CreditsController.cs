using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace laba3.Controllers;

[ApiController]
[Route("api/[controller]")]
public sealed class CreditsController : ControllerBase
{
    private readonly AppDbContext _context;

    public CreditsController(AppDbContext context)
    {
        _context = context;
    }

    [HttpGet]
    public async Task<ActionResult<IEnumerable<CreditEntity>>> GetCredits()
        => await _context
            .Credits
            .AsNoTracking()
            .ToListAsync();

    [HttpGet("{id:int}")]
    public async Task<ActionResult<CreditEntity>> GetCredit(int id)
    {
        var credit = await _context.Credits.FindAsync(id);
        
        return credit == null ? NotFound() : credit;
    }

    [HttpPost]
    public async Task<ActionResult<CreditEntity>> CreateCredit(CreditEntity credit)
    {
        _context.Credits.Add(credit);
        
        await _context.SaveChangesAsync();
        
        return Ok(credit);
    }

    [HttpPut("{id:int}")]
    public async Task<IActionResult> UpdateCredit(int id, CreditEntity credit)
    {
        var existing = await _context.Credits.FindAsync(id);
        
        if (existing == null)
        {
            return NotFound();
        }

        existing.Name = credit.Name;
        existing.Amount = credit.Amount;
        existing.InterestRate = credit.InterestRate;
        existing.IssueDate = credit.IssueDate;
        existing.TermMonths = credit.TermMonths;

        await _context.SaveChangesAsync();
        
        return NoContent();
    }


    [HttpDelete("{id:int}")]
    public async Task<IActionResult> DeleteCredit(int id)
    {
        var credit = await _context.Credits.FindAsync(id);
        
        if (credit == null)
        {
            return NotFound();
        }

        _context.Credits.Remove(credit);
        await _context.SaveChangesAsync();

        return NoContent();
    }
}
