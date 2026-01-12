import re
import os

markdown_table_content = """
| File Path | Content Type | Categories | Existing Tags | Proposed Tags |
| :--- | :--- | :--- | :--- | :--- |
| `content/about.md` | Page | (none) | (none) | (none) |
| `content/lab/category-vs-tag/index.md` | lab | (none) | `taxonomy`, `categories`, `tags`, `hugo` | `systems-thinking`, `hugo`, `taxonomy` |
| `content/signals/signals-week-02-2026/index.md` | signals | (none) | `entrepreneurship`, `capital-allocation`, `long-term-thinking` | `capital-allocation`, `long-term-thinking`, `venture-building` |
| `content/articles/a16z-library/index.md` | articles | `Essays` | `External`, `VC`, `Management` | `a16z`, `venture-capital`, `reading-list`, `mental-models` |
| `content/articles/air-space/index.md` | articles | `Strategy` | `External`, `Digital`, `Banking`, `AI` | `platform-economics`, `ben-thompson`, `aggregation-theory`, `artificial-intelligence` |
| `content/articles/asian-banker-future-of-banking/index.md` | articles | `Fintech` | `External`, `AI`, `DeFi`, `CBDC`, `Digital Transformation`, `Fintech`, `Banking` | `artificial-intelligence`, `stablecoins`, `open-finance`, `digital-transformation`, `systems-thinking` |
| `content/articles/cbdc/index.md` | articles | `Fintech` | `CBDC`, `Fintech`, `Monetary Policy`, `Blockchain`, `Economics` | `stablecoins`, `monetary-policy`, `blockchain`, `incentive-design` |
| `content/articles/decoupling/index.md` | articles | `Strategy` | `External`, `Design`, `Management`, `Strategy` | `organizational-design`, `systems-thinking`, `long-term-thinking` |
| `content/articles/deleted-emails/index.md` | articles | `Strategy` | `Digital Transformation`, `AI`, `Governance`, `Leadership`, `Strategy` | `board-governance`, `organizational-design`, `artificial-intelligence`, `digital-transformation` |
| `content/articles/discovery-to-knowledge/index.md` | articles | `Technology` | `GenAI`, `Software Engineering`, `Digital Transformation`, `Technology Leadership`, `AI`, `Systems Thinking`, `Innovation` | `systems-thinking`, `artificial-intelligence`, `second-brain`, `knowledge-management` |
| `content/articles/erpx/index.md` | articles | `Venture Building` | `Fintech`, `SME`, `ERP`, `AI`, `Venture Building`, `Transformation` | `venture-building`, `embedded-finance`, `platform-economics`, `smb` |
| `content/articles/future-of-finance/index.md` | articles | `Fintech` | `External`, `Digital`, `Banking`, `Open Finance`, `DeFi`, `Embedded Finance` | `open-finance`, `embedded-finance`, `payments`, `stablecoins` |
| `content/articles/git-design/index.md` | articles | `Technology` | `Technology`, `Design` | `git`, `design-systems`, `systems-thinking` |
| `content/articles/mit-ai-report-2025/index.md` | articles | `Strategy` | `AI`, `Strategy`, `Digital Transformation`, `Leadership` | `artificial-intelligence`, `long-term-thinking`, `digital-transformation`, `reading-list`, `mit` |
| `content/articles/newspapers-insurance/index.md` | articles | `Strategy` | `External`, `Digital`, `Insurance`, `Strategy` | `insurtech`, `embedded-finance`, `digital-transformation` |
| `content/articles/path-to-scale/index.md` | articles | `Venture Building` | `External`, `Strategy`, `Scale`, `Fintech`, `Leadership` | `venture-building`, `go-to-market`, `organizational-design`, `platform-economics` |
| `content/articles/pilot-purgatory/index.md` | articles | `Strategy` | `AI`, `Strategy`, `Digital Transformation`, `Leadership` | `venture-building`, `g-to-market`, `incentive-design`, `organizational-design` |
| `content/articles/prediction-market/index.md` | articles | `Venture Building` | `Venture Building`, `Strategy`, `Venture Capital`, `Prediction Markets` | `prediction-markets`, `venture-building`, `capital-allocation`, `systems-thinking` |
| `content/articles/r-packages/index.md` | articles | `Technology` | `External`, `Technology`, `Machine Learning` | `r`, `open-source`, `data-science`, `programming` |
| `content/articles/responsiveness/index.md` | articles | `Leadership` | `Productivity`, `Management`, `Customer Experience`, `Operations` | `organizational-design`, `asynchronous-work`, `productivity` |
| `content/articles/simulation-standard/index.md` | articles | `Technology` | `BPM`, `Workflow`, `Automation`, `Simulation`, `Optimization` | `simulation`, `digital-twin`, `systems-thinking`, `bpm` |
| `content/articles/strategy-prework/index.md` | articles | `Strategy` | `strategy`, `leadership`, `governance`, `digital transformation` | `board-governance`, `long-term-thinking`, `systems-thinking`, `digital-transformation` |
| `content/articles/the-inevitable/index.md` | articles | `Essays` | `Futurism`, `Book Reviews`, `AI`, `Technology Trends`, `Society` | `kevin-kelly`, `long-term-thinking`, `artificial-intelligence`, `systems-thinking`, `reading-list` |
| `content/articles/top-podcasts-2025/index.md` | articles | `Essays` | `Startups`, `Fintech`, `AI`, `Strategy`, `Technology`, `Trends`, `History`, `Podcasts` | `reading-list`, `podcasts`, `venture-capital`, `artificial-intelligence`, `long-term-thinking` |
| `content/articles/values/index.md` | articles | `Leadership` | `strategy`, `values`, `leadership`, `talent`, `transformation`, `governance` | `organizational-design`, `board-governance`, `long-term-thinking` |
| `content/articles/x402-intro/index.md` | articles | `Fintech` | `stablecoins`, `fintech`, `payments`, `digital transformation`, `AI` | `stablecoins`, `payments`, `digital-transformation`, `artificial-intelligence` |
| `content/articles/yap-stone-money/index.md` | articles | `Fintech` | `Money`, `Blockchain`, `Fintech`, `Cryptocurrency`, `Economics` | `money`, `systems-thinking`, `long-term-thinking`, `blockchain` |
| `content/contact.md` | Page | (none) | (none) | (none) |
| `content/lab/pyenv/index.md` | lab | (none) | `Python`, `Software Engineering`, `DevOps`, `AI`, `Vibe Coding`, `Open Source`, `Programming` | `python`, `open-source`, `programming`, `dev-ops`, `software-engineering` |
| `content/portfolio/akin/index.md` | portfolio | (none) | `RegTech`, `eKYC`, `Identity` | `regtech`, `identity`, `ekyc` |
| `content/portfolio/artifract/index.md` | portfolio | (none) | `Web3`, `NFT`, `Wealth` | `web3`, `nft`, `asset-management` |
| `content/portfolio/assured/index.md` | portfolio | (none) | `InsurTech`, `Embedded Finance`, `API`, `Financial Inclusion` | `insurtech`, `embedded-finance`, `api-economy`, `financial-inclusion` |
| `content/portfolio/biddit/index.md` | portfolio | (none) | `PropTech`, `Real Estate`, `Fractional Ownership`, `Web3` | `proptech`, `real-estate`, `tokenization`, `web3` |
| `content/portfolio/bux/index.md` | portfolio | (none) | `Fintech`, `Payments`, `E-Commerce`, `MSME` | `payments`, `smb`, `e-commerce` |
| `content/portfolio/cardano/index.md` | portfolio | (none) | `Blockchain`, `Web3`, `DeFi` | `blockchain`, `web3`, `defi` |
| `content/portfolio/cashbux/index.md` | portfolio | (none) | `Agency Banking`, `Financial Inclusion`, `MSME`, `POS` | `agency-banking`, `financial-inclusion`, `smb`, `payments` |
| `content/portfolio/commisari/index.md` | portfolio | (none) | `FoodTech`, `AgriTech`, `Supply Chain`, `MSME` | `foodtech`, `agritech`, `supply-chain`, `smb` |
| `content/portfolio/consensys/index.md` | portfolio | (none) | `Web3`, `Infrastructure`, `Ethereum`, `Wallet` | `web3`, `ethereum`, `metamask` |
| `content/portfolio/dragonpay/index.md` | portfolio | (none) | `Fintech`, `Payments`, `E-Commerce` | `payments`, `e-commerce` |
| `content/portfolio/erpx/index.md` | portfolio | (none) | `ERP`, `MSME`, `Finance`, `Digital` | `smb`, `erp`, `saas` |
| `content/portfolio/finscore/index.md` | portfolio | (none) | `Fintech`, `Credit Scoring`, `AI`, `Big Data` | `credit-scoring`, `artificial-intelligence`, `lending` |
| `content/portfolio/i2i/index.md` | portfolio | (none) | `BaaS`, `Blockchain`, `Stablecoins` | `banking-as-a-service`, `blockchain`, `stablecoins` |
| `content/portfolio/klaytyn/index.md` | portfolio | (none) | `Blockchain`, `Infrastructure`, `Enterprise DLT` | `blockchain`, `web3`, `enterprise-dlt` |
| `content/portfolio/manulife-trust/index.md` | portfolio | (none) | `Asset Management`, `Trust Corporation`, `Wealth` | `asset-management`, `wealth-management` |
| `content/portfolio/pdax/index.md` | portfolio | (none) | `Fintech`, `Cryptocurrency`, `Digital Assets`, `Web3` | `digital-assets`, `crypto-exchange`, `web3` |
| `content/portfolio/seekcap/index.md` | portfolio | (none) | `Fintech`, `Lending`, `MSME`, `AI` | `lending`, `smb`, `artificial-intelligence` |
| `content/portfolio/sentro/index.md` | portfolio | (none) | `E-Commerce`, `MSME`, `SaaS`, `Embedded Finance` | `smb`, `e-commerce`, `saas`, `embedded-finance` |
| `content/portfolio/solviva/index.md` | portfolio | (none) | `CleanTech`, `Distributed Energy`, `Energy Transition`, `Consumer Finance`, `Solar` | `solar`, `electric-vehicles`, `energy-markets`, `project-finance` |
| `content/portfolio/splix/index.md` | portfolio | (none) | `Fintech`, `Open Finance`, `BNPL`, `Payments` | `open-finance`, `payments`, `lending`, `bnpl` |
| `content/portfolio/vinne/index.md` | portfolio | (none) | `Web3`, `DeFi`, `Wealth` | `web3`, `defi`, `asset-management` |
| `content/portfolio/voltai/index.md` | portfolio | (none) | `Energy Transition`, `Distributed Energy`, `Electric Vehicles`, `CleanTech` | `electric-vehicles`, `energy-markets`, `project-finance` |
| `content/portfolio/xlog/index.md` | portfolio | (none) | `Logistics`, `Supply Chain Finance`, `Blockchain`, `Embedded Finance` | `supply-chain`, `logistics`, `embedded-finance`, `blockchain` |
| `content/portfolio/xpanse/index.md` | portfolio | (none) | `Open Finance`, `API`, `BaaS`, `Infrastructure` | `open-finance`, `banking-as-a-service`, `api-economy` |
| `content/videos/next-gen-bank-tech/index.md` | videos | `Fintech` | `Technology`, `Transformation`, `History`, `Banking`, `AI` | `digital-transformation`, `artificial-intelligence`, `systems-thinking` |
| `content/videos/open-finance-anc/index.md` | videos | `Fintech` | `Digital`, `Open Finance`, `Embedded Finance`, `AI` | `open-finance`, `embedded-finance`, `artificial-intelligence` |
| `content/videos/proptech/index.md` | videos | `Fintech` | `PropTech`, `Tokenization`, `Blockchain`, `Embedded Finance`, `Wealth` | `proptech`, `tokenization`, `embedded-finance`, `asset-management` |
"""

def parse_markdown_table(md_table_content):
    lines = md_table_content.strip().split('\n')
    header = [h.strip() for h in lines[0].split('|')[1:-1]]
    data = []
    for line in lines[2:]:
        values = [v.strip() for v in line.split('|')[1:-1]]
        data.append(dict(zip(header, values)))
    return data

# Parse the markdown table from the content provided
processed_files_data = parse_markdown_table(markdown_table_content)

updated_table_lines = []
updated_table_lines.append("| File Path | Content Type | Categories | Existing Tags | Proposed Tags |")
updated_table_lines.append("| :--- | :--- | :--- | :--- | :--- |")

for row in processed_files_data:
    file_path = row['File Path']
    content_type = row['Content Type']
    categories = row['Categories']
    existing_tags = row['Existing Tags']
    
    # Remove 'venture-building' from proposed tags if it exists
    proposed_tags_str = row['Proposed Tags']
    proposed_tags_list = [tag.strip().replace('`', '') for tag in proposed_tags_str.split(',')] if proposed_tags_str != '(none)' else []
    
    cleaned_proposed_tags = [tag for tag in proposed_tags_list if tag.lower() != 'venture-building']
    
    # Reconstruct the proposed tags string in markdown format
    if not cleaned_proposed_tags:
        new_proposed_tags_md = '(none)'
    else:
        new_proposed_tags_md = ', '.join([f'`{tag}`' for tag in cleaned_proposed_tags])
    
    updated_table_lines.append(f"| {file_path} | {content_type} | {categories} | {existing_tags} | {new_proposed_tags_md} |")

# Join the updated lines to form the new markdown table content
new_markdown_table_content = "\n".join(updated_table_lines)

# Write the new content back to tag_governance_proposal.md
with open("tag_governance_proposal.md", "w") as f:
    f.write(new_markdown_table_content)

print("Updated tag_governance_proposal.md with 'venture-building' removed from proposed tags.")
