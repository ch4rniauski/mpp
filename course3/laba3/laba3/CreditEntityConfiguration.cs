using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;

namespace laba3;

public class CreditEntityConfiguration : IEntityTypeConfiguration<CreditEntity>
{
    public void Configure(EntityTypeBuilder<CreditEntity> builder)
    {
        builder.HasKey(c => c.Id);

        builder
            .Property(c => c.Id)
            .ValueGeneratedOnAdd();

        builder
            .Property(c => c.Name)
            .HasMaxLength(200)
            .IsRequired(false);

        builder
            .Property(c => c.Amount)
            .IsRequired();

        builder
            .Property(c => c.InterestRate)
            .IsRequired();

        builder
            .Property(c => c.IssueDate)
            .HasColumnType("date")
            .IsRequired();

        builder
            .Property(c => c.TermMonths)
            .IsRequired();
    }
}