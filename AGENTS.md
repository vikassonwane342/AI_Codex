# Repository Guidelines

## Project Structure & Module Organization
This repository is a .NET Web API solution with the main service in `CarMarketplace.Api/`. Source code is organized by layer: `Controllers/` (HTTP endpoints), `Services/` (business logic), `Repositories/` (data access), `Dtos/`, `Entities/`, and cross-cutting concerns in `Configuration/` and `Middleware/`. Reference docs live in `docs/` (architecture, conventions, flows, project overview). Database scripts are in `script.sql`.

## Build, Test, and Development Commands
Use the solution file at the repo root.
- `dotnet build Ai.sln` builds all projects.
- `dotnet run --project CarMarketplace.Api/CarMarketplace.Api.csproj` runs the API locally; Swagger UI is served at `/swagger`.
- `dotnet restore` restores NuGet packages if needed.
There is no test project yet, so `dotnet test` will not run anything until tests are added.

## Architecture & Flows
Architecture follows Clean Architecture with a Controller to Service to Repository call chain. The backend is ASP.NET Core Web API (.NET 10) using Dapper with SQL Server. Keep controllers thin and move business rules to services. Key flows:
- Car listing: seller logs in, creates listing, adds details, listing becomes visible.
- Booking: buyer selects a car, confirms booking, order is created.

## Coding Style & Naming Conventions
Follow the conventions in `docs/convensions.md`.
- Indentation: 4 spaces in C#.
- Naming: Classes/Methods `PascalCase`, variables `camelCase`, interfaces prefixed with `I` (e.g., `IAuthService`).
- API rules: use DTOs for request/response models, validate inputs, return correct HTTP status codes.
- Data access: use Dapper; keep controllers thin and business logic in services.

## Testing Guidelines
No testing framework is configured yet. When adding tests, keep them in a `*.Tests` project (e.g., `CarMarketplace.Api.Tests`) and use `dotnet test` from the repo root. Name test classes and methods clearly (e.g., `CarServiceTests`, `CreateListing_WhenInvalid_ReturnsError`).

## Commit & Pull Request Guidelines
There is no Git history in this repository yet, so no commit message conventions are established. Use concise, imperative messages (e.g., `Add car listing validation`). For PRs, include:
- A clear description of the change and scope.
- Linked issue or requirement if applicable.
- Any API behavior changes and updated Swagger or request examples.

## Skills & Reference Docs
When unsure about architecture or functionality, consult:
- `docs/architecture.md` for layering rules and naming patterns.
- `docs/flows.md` for business flows.
- `docs/convensions.md` for coding rules.
- `docs/project.md` for domain scope.
Agent skills are in `skills/`:
- `skills/api-generator.md` for creating new API endpoints.
- `skills/bug-fixer.md` for minimal, focused fixes.

## Security & Configuration Notes
Configuration is in `CarMarketplace.Api/appsettings.json` and `appsettings.Development.json`. Do not commit secrets. Ensure the SQL Server connection string and JWT settings are supplied via user secrets or environment variables for local development.
