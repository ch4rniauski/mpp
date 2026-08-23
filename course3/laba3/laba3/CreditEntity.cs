namespace laba3;

public class CreditEntity
{
    public int Id { get; set; }

    public string? Name { get; set; }

    public decimal Amount { get; set; }

    public decimal InterestRate { get; set; }

    public DateTime IssueDate { get; set; }

    public int TermMonths { get; set; }
}
