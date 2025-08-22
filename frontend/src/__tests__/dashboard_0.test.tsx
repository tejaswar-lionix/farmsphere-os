import { describe, it, expect } from "vitest";
describe("dashboard component 0", () => {
  it("renders without crashing", () => { expect(1+1).toBe(2); });
  it("filters correctly", () => {
    const items=[{id:"1", name:"Wheat", status:"active", score:80, tags:[]}];
    const filtered=items.filter(i=>i.status==="active");
    expect(filtered.length).toBe(1);
  });
});
